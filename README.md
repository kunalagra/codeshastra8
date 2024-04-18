<h1 align="center">
  <br>
  <a href="https://sleep-tracking-cs8.onrender.com/"><img src="https://github.com/kunalagra/codeshastra8/blob/main/static/img/undraw_sleep_analysis_o-5-f9.svg" alt="Personalized Insurance Premium" width="200"></a>
  <br>
  Sleep Monitoring using Cam
  <br>
</h1>

<h4 align="center">Find your sleep pattern</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/kunalagra/codeshastra8/main/static/img/screenshot.jpeg)

## Key Features

- Record video using a webcam on a laptop covering the sleeping area of the individual 
- Consider low light conditions and perform image cleanup for better object detection
- Detect motion of the individual and create a log of movements with the duration of movement & the quantum of movement 
- Plot sleeping pattern of the individual showing pattern in timings of the movements, hours of uninterrupted sleep, wake up time pattern etc.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) & [Python](https://www.python.org/) installed. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/kunalagra/codeshastra8

# Go into the repository
$ cd codeshastra8

# Install dependencies
$ pip install -r requirements.txt

# Rename .env.example to .env
$ mv .env.example .env

# Run the server
$ flask run 
```
> [!IMPORTANT]  
> Populate your .env keys with their respective values. 

> [!NOTE]
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.

## Credits

This software uses the following packages:

- [Python](https://www.python.org/)
- [Bootstrao](https://react.dev/)
- Built at Codeshastra8 - DJ Sanghvi


## You may also like...

- [SumUp](https://github.com/kunalagra/SumUp) - Summarize TEAMs Meeting
- [Codegamy](https://github.com/kunalagra/codegamy) - A LeetCode clone

## License

AGPL-3

