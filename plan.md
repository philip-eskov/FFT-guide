# Tentative structure: 

## Theory 

### 1) Intoduction
 
- Motivation 
- Prerequsite knowledge
	- Complex numbers 
	- Basic (MAT1100) calculus 
	- Properties of sines and cosines
		- Phase
		- Amplitude 
		- Frequency 

### 2) What is frequency domain? 

- Intutitve explenation 
- Give some motivational examples
	- Sound from a piano chord over time (easy to grasp)
	- Frequency components of EM wave (relevant to physics / chemistry(?))

### 3) The Fourier transfrom 

- Mathematical definition 
- Focus on intution 
- Explain information of complex values 
	- Abs = frequency response
	- imaginary part needed for phase response 

### 4) The discrete Fourier transform (DFT) 

- Why do we need to use the DFT and not the continious Fourier transform? 
- Mathematical definition
	- Explain changes in expression from contninous to discrete
- Some words on the FFT 

### 5) Sampling frequency and aliasing 
- Nyq. limit / frequency 
- What is aliasing 

### 6) (optional) Why does aliasing occur? 
- Introduce Ш function 
- Bigger in sampling period in TD (wider Ш) = tighter Ш in FD = closer spaced aliases 

## Implementing the FFT in Python 

### 7) Scipy, numpy and matplotlib 

### 8) Relevant constants
 
- Sampling rate
- N samples 

### 9) Taking the FFT 
- Defining the x-axis of frequency domain 
	- sp.fft.fftfreq and why the parameters are chosen in they way that they are 
- Taking the FFT 
	- sp.fft.fft 
	- Normalising the absolute value

- Plotting
	- Limiting the x-axis (negative frequencies are weird) 
