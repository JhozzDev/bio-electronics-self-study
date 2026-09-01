# Bioelectronics Learning Path

A self-paced, 50-week roadmap for learning **Biomedical Electronics Engineering** from first principles — 2 hours/day, 6 days/week — culminating in a fully integrated capstone project.

This repo documents the plan, tracks progress, and hosts the code produced along the way (circuit analysis, filter design, biosignal processing, embedded firmware, and a final Streamlit dashboard).

## Why this repo exists

This isn't just a study log — it's a portfolio artifact. Planning, discipline, and the ability to break a large domain (electronics + DSP + biomedical instrumentation + embedded systems + applied ML) into a structured, executable curriculum is itself evidence of engineering capability.

## How the roadmap is structured

- **Duration:** 50 weeks, ~2 hours of focused study per day
- **Cadence:** 6 study days per week; the 7th day is rest or light review (not scheduled)
- **Granularity:** Each day pairs one concept with one concrete exercise — theory/reading (45–60 min) followed by problem-solving, simulation, or code
- **Checkpoints:** Every phase ends with a self-assessment (0–5 scale) across its core topics. Progression to the next phase is gated on scoring ≥3 in critical fundamentals
- **Flexibility:** The calendar is a guide, not a straitjacket — topics can take longer than a day, but the dependency order between topics should be respected

## Phases

| Phase | Weeks | Focus |
|---|---|---|
| 1 | 1–6 | Fundamentals of electricity and electronics (Ohm's law, Kirchhoff's laws, nodal/mesh analysis, RC/RL/RLC transients, Thévenin/Norton, phasors) |
| 2 | 7–12 | Analog electronics (diodes and rectification, BJT, MOSFET, op-amps, instrumentation amplifiers, active filters) |
| 3 | 13–16 | Digital electronics (combinational and sequential logic, FSMs, memories, peripherals: GPIO/PWM/UART/SPI/I2C, ADC/DAC) |
| 4 | 17–22 | Signals and systems (Fourier series, Fourier transform and FFT, convolution and LTI systems, sampling/Nyquist/aliasing) |
| 5 | 23–27 | Digital signal processing with Python (NumPy/Matplotlib/Pandas, FIR/IIR filter design, FFT-based analysis, feature extraction) |
| 6 | 28–32 | Biomedical signals (ECG and the Pan-Tompkins algorithm, HRV analysis, EEG, EMG, PPG) |
| 7 | 33–37 | Biomedical instrumentation (sensors and transducers, electrical safety and isolation, system noise budgets, real-world datasheets, front-end design) |
| 8 | 38–41 | Applied embedded systems (MCU architecture, Wokwi simulation, interrupts and circular buffers, serial communication) |
| 9 | 42–45 | Scientific computing and biomedical data (public datasets, batch processing, feature engineering, basic classification) |
| Capstone | 46–49 | Full-stack integration: analog design → firmware → signal processing → Streamlit dashboard → documentation |

Days 7 of each week (rest/light review) and the final 30-day plan (week 50+: portfolio, interview prep, applications) are covered in the companion file `roadmap_bioelectronica.md`.

## Projects

Hands-on projects are built incrementally throughout the roadmap and consolidated during the capstone phase:

| # | Project | Phase |
|---|---|---|
| 1 | `circuit-transient-analyzer` | 1 |
| 2 | `biopotential-instrumentation-amp` | 2 |
| 3 | `biomedical-filter-designer` | 5 |
| 4 | `vital-signs-alarm-fsm` | 3 |
| 5 | `spectral-analysis-toolkit` | 4 |
| 6 | `qrs-detector-pan-tompkins` | 6 |
| 7 | `hrv-analysis` | 6 |
| 8 | `emg-eeg-denoising` | 6 |
| 9 | `ecg-daq-system-simulation` | 7 |
| 10 | `ppg-embedded-acquisition-sim` | 8 |
| 11 | `ecg-arrhythmia-classifier` | 9 |
| — | **Capstone**: integrated ECG pipeline with Streamlit dashboard | Capstone |

## Tools and stack

- **Circuit simulation:** LTspice
- **Digital logic simulation:** Logisim Evolution
- **Embedded simulation:** Wokwi (ESP32)
- **Signal processing:** Python, NumPy, SciPy, Pandas, Matplotlib, SymPy
- **Biomedical data:** PhysioNet / MIT-BIH via `wfdb`, EEG via `mne`, HRV via `neurokit2`
- **Machine learning:** scikit-learn
- **Dashboard:** Streamlit
- **Version control:** Git / GitHub, with each project pushed as its own milestone


## Progress tracking

Each phase closes with a self-assessment checkpoint (0–5) on its core topics. Suggested tracking approach:

- [ ] Phase 1 — Fundamentals of electricity and electronics
- [ ] Phase 2 — Analog electronics
- [ ] Phase 3 — Digital electronics
- [ ] Phase 4 — Signals and systems
- [ ] Phase 5 — DSP with Python
- [ ] Phase 6 — Biomedical signals
- [ ] Phase 7 — Biomedical instrumentation
- [ ] Phase 8 — Applied embedded systems
- [ ] Phase 9 — Scientific computing and biomedical data
- [ ] Capstone — Full integration + dashboard + documentation

*This roadmap and calendar were designed as a structured path from electronics fundamentals to a working, portfolio-ready biomedical signal processing system — intended to serve as evidence of planning and follow-through when applying for internships or entry-level roles in biomedical/embedded engineering.*
