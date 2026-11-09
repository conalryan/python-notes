//! A standalone Rust producer: synthesize a quiet tone and write standard PCM WAV.

use std::error::Error;
use std::f32::consts::TAU;
use std::fs::OpenOptions;
use std::io::BufWriter;

fn main() -> Result<(), Box<dyn Error>> {
    let path = std::env::args().nth(1).ok_or("provide an output WAV path")?;
    let sample_rate = 48_000_u32;
    let samples: Vec<f32> = (0..sample_rate)
        .map(|frame| 0.2 * (TAU * 440.0 * frame as f32 / sample_rate as f32).sin())
        .collect();
    let samples = rusty_audio::gain_samples(&samples, -3.0)?;
    let specification = hound::WavSpec {
        channels: 1,
        sample_rate,
        bits_per_sample: 16,
        sample_format: hound::SampleFormat::Int,
    };
    // create_new protects an existing master; hound writes the WAV container.
    let file = OpenOptions::new().write(true).create_new(true).open(path)?;
    let mut writer = hound::WavWriter::new(BufWriter::new(file), specification)?;
    for sample in samples {
        // Quantize only at export, after DSP. This teaching tone does not add dither.
        writer.write_sample((sample.clamp(-1.0, 1.0) * i16::MAX as f32).round() as i16)?;
    }
    writer.finalize()?;
    Ok(())
}