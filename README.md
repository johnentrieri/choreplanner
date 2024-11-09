# Chore Planner

Simple planner application for creating a chore schedule

## Description

TBD

## Getting Started

### Dependencies

* [Raspberry Pi OS](https://www.raspberrypi.com/)
	* Raspberry Pi 5
	* Kernel Version 6.6 / Debian Version 12 (bookworm)
* [OpenAPI Generator](https://openapi-generator.tech/)
	* Requires the following installed for the [Bash Launcher Script](https://openapi-generator.tech/docs/installation#bash-launcher-script) to work
		* [Java JDK](https://www.oracle.com/java/technologies/downloads/)
		* [Maven](https://maven.apache.org/)
		* [JQ](https://jqlang.github.io/jq/)
		* [Curl](https://curl.se/)
* [Python](https://www.python.org/downloads/)
	* python3 Version 3.11.2
	* pip3 Version 23.0.1


### Installing

#### Server
Clone Repository:
```bash
git clone https://github.com/johnentrieri/choreplanner.git
```
Generate Server Code Automatically using OpenAPI Spec:
```bash
cd choreplanner
./generate-server-code
```
Create & Activate Virtual Environment:
```bash
cd server
python3 -m venv venv
. venv/bin/activate
```
Install & Launch Server
```bash
pip3 install -r requirements.txt
python3 -m openapi_server
```
Test Server is Running at http://localhost:8080/ui
```bash
pip3 install -r requirements.txt
python3 -m openapi_server
```
#### Client
TBD

### Usage

TBD

## Help

TBD

## Contributors & Maintainers

Contributors names and contact info

* [John Entrieri](https://github.com/johnentrieri)

## Version History

* 0.1
    * Initial Release
