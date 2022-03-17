# RPiGPIO WebRemote

Controll your Raspberry Pi's GPIO pins from a simple web app

![](https://github.com/Proactive-Development/RPi-GPIO-WebRemote/blob/main/demo.png)

## How to install and run

- Boot up raspbian with graphics
- Download the Souce code
- Install the dependancies that are required

## Usage
To use RPiGPIO WebRemote you will need a browser or a http client

### Web App (In Development)
To connect to the web app go the address

`localhost:3000` 

**Note**: Port can be changed in the settings


### API
Using a web browser or http client you can use the `/set` page to set a gpio pin

#### Arguments
| Name | Function  |
| ------------ | ------------ |
| Pin | Chose whitch pin to set|
| Mode | Set the pin HIGH or LOW. (Must be typed high and low)|

## Depandancies
- JsonReg `pip install jsonreg`

