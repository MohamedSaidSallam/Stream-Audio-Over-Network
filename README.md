# Stream Audio Over Network [NOT SUPPORTED]

[![GitHub Release][github_release_badge]][github_release_link]
[![License][license-image]][license-url]

A simple python project to stream audio over the network. Mainly made so I can stream my laptop's audio to my PC with minimum quality loss.

> NOT SUPPORTED: check [Known Issues](##Known-Issues) section.

## Features

* Stream Audio over network
* Scan for compatable audio devies
* GUI for device and port selection
* Port forwarding for windows

![SendAudio](docs/SendAudio.png)
![ReceiveAudio](docs/ReceiveAudio.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```sh
pip install -r requirements.txt
```

A [fork of PyAudio](https://github.com/intxcc/pyaudio_portaudio) that allows loopback of audio. A compiled version can be download from [the original authors repo's releases](https://github.com/intxcc/pyaudio_portaudio/releases).

```sh
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

#### Use the install.bat script for windows

The following can also be found in install.bat file.

```batch
py -3.7 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe -m pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

### Running the Code

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```sh
venv\Scripts\python.exe -m StreamAudioOverNetwork
```

Or you can use the run.bat file.

### Example

Text

## Known Issues

* If no connection is made after clicking, The receive audio button the receive audio thread won't terminate as it won't reach the termination flag so even if the GUI is closed the thread remains.
* After a random period, The data transfer will skip a part and get desynced and may suddenly start playing distorted audio until restarted.

## Built With

* [VS Code](https://code.visualstudio.com/) - Code Editor

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository][github-tags].

## Authors

* **Mohamed Said Sallam** - Main Dev - [TheDigitalPhoenixX](https://github.com/TheDigitalPhoenixX)

See also the list of [contributors][github-contributors] who participated in this project and their work in [CONTRIBUTORS.md](CONTRIBUTORS.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [Original Source Code](https://www.reddit.com/r/learnpython/comments/ak7dih/how_to_play_audio_as_its_being_received_over_a/) that helped me start.

[license-image]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[license-url]: https://opensource.org/licenses/MIT

[github_release_badge]: https://img.shields.io/github/v/release/TheDigitalPhoenixX/Stream-Audio-Over-Network.svg?style=flat&include_prereleases
[github_release_link]: https://github.com/TheDigitalPhoenixX/Stream-Audio-Over-Network/releases

[github-contributors]: https://github.com/TheDigitalPhoenixX/Stream-Audio-Over-Network/contributors
[github-tags]: https://github.com/TheDigitalPhoenixX/Stream-Audio-Over-Network/tags
