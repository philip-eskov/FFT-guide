# Tentative structure: 

## Theory 

### 1) Introduction
 
- Motivation 
- Prerequisite knowledge
	- Complex numbers 
	- Basic (MAT1100) calculus 
	- Properties of sines and cosines
		- Phase
		- Amplitude 
		- Frequency 

### 2) What is frequency domain? 

- Intuitive explanation 
- Give some motivational examples
	- Sound from a piano chord over time (easy to grasp)
	- Frequency components of EM wave (relevant to physics / chemistry(?))

### 3) The Fourier transform  

- Mathematical definition 
- Focus on intuition 
- Explain information of complex values 
	- Abs = frequency response
	- imaginary part needed for phase response 

### 4) The discrete Fourier transform (DFT) / Sampling frequency and aliasing 

- Why do we need to use the DFT and not the continuous Fourier transform? 
- Mathematical definition
	- Explain changes in expression from continuous to discrete
- Some words on the FFT 
- Nyq. limit / frequency 
- What is aliasing 

### 5) Implementing the FFT in Python
- Prerequisites
	- Scipy, numpy and matplotlib imports 
	- Relevant constants
	- Sampling rate
	- N samples 

- Taking the FFT 
	- Defining the x-axis of frequency domain 
		- sp.fft.fftfreq and why the parameters are chosen in they way that they are 
	- Taking the FFT 
		- sp.fft.fft 
		- Normalizing the absolute value
	- Plotting
		- Limiting the x-axis (negative frequencies are weird) 

### 6) FAQ

### 7) Further reading

### 7) Glossary 