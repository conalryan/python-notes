//! Offline DSP on owned buffers. No Python objects are touched while detached.

fn validate(samples: &[f32]) -> Result<(), &'static str> {
    if samples.is_empty() || samples.iter().any(|sample| !sample.is_finite()) {
        return Err("samples must be nonempty and finite");
    }
    Ok(())
}

/// Borrow the input, return an owned result, and report invalid data with Result.
pub fn gain_samples(samples: &[f32], decibels: f32) -> Result<Vec<f32>, &'static str> {
    validate(samples)?;
    if !decibels.is_finite() || !(-120.0..=60.0).contains(&decibels) {
        return Err("gain must be finite and between -120 and 60 dB");
    }
    let multiplier = 10.0_f32.powf(decibels / 20.0);
    let output: Vec<f32> = samples.iter().map(|sample| sample * multiplier).collect();
    validate(&output)?;
    Ok(output)
}

/// This is sample-peak normalization, not a limiter or LUFS mastering algorithm.
pub fn normalize_samples(samples: &[f32], target_dbfs: f32) -> Result<Vec<f32>, &'static str> {
    validate(samples)?;
    if !target_dbfs.is_finite() || !(-120.0..=0.0).contains(&target_dbfs) {
        return Err("target must be finite and between -120 and 0 dBFS");
    }
    let peak = samples.iter().map(|sample| sample.abs()).fold(0.0_f32, f32::max);
    if peak == 0.0 {
        return Ok(samples.to_vec());
    }
    let target = 10.0_f32.powf(target_dbfs / 20.0);
    // Divide before multiplying to avoid overflow when normalizing very quiet audio.
    Ok(samples.iter().map(|sample| (sample / peak) * target).collect())
}

// Keeping Python bindings behind a feature lets cargo test run the Rust core
// without linking an embedded Python interpreter or an extension module.
#[cfg(feature = "python")]
#[pyo3::pymodule]
mod rusty_audio {
    use pyo3::exceptions::PyValueError;
    use pyo3::prelude::*;

    #[pyfunction]
    fn gain(py: Python<'_>, samples: Vec<f32>, decibels: f32) -> PyResult<Vec<f32>> {
        // Vec owns its data; detaching cannot leave a borrowed Python buffer racing
        // with another Python thread. Extraction and returning the list still copy.
        py.detach(move || super::gain_samples(&samples, decibels))
            .map_err(PyValueError::new_err)
    }

    #[pyfunction]
    fn normalize(py: Python<'_>, samples: Vec<f32>, target_dbfs: f32) -> PyResult<Vec<f32>> {
        py.detach(move || super::normalize_samples(&samples, target_dbfs))
            .map_err(PyValueError::new_err)
    }
}

#[cfg(test)]
mod tests {
    use super::{gain_samples, normalize_samples};

    #[test]
    fn gain_is_identity_at_zero_db() {
        assert_eq!(gain_samples(&[0.25, -0.5], 0.0).unwrap(), vec![0.25, -0.5]);
    }

    #[test]
    fn silence_does_not_divide_by_zero() {
        assert_eq!(normalize_samples(&[0.0, 0.0], -1.0).unwrap(), vec![0.0, 0.0]);
    }

    #[test]
    fn normalization_preserves_polarity_and_relative_amplitude() {
        let output = normalize_samples(&[-2.0, 1.0], -6.0).unwrap();
        assert!((output[0] + 10.0_f32.powf(-6.0 / 20.0)).abs() < 1e-6);
        assert!((output[1] / output[0] + 0.5).abs() < 1e-6);
    }

    #[test]
    fn invalid_input_returns_errors_not_panics() {
        assert!(gain_samples(&[], 0.0).is_err());
        assert!(gain_samples(&[f32::NAN], 0.0).is_err());
        assert!(gain_samples(&[0.5], f32::INFINITY).is_err());
        assert!(gain_samples(&[f32::MAX], 60.0).is_err());
        assert!(normalize_samples(&[0.5], 1.0).is_err());
    }
}