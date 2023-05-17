# Akai MPK Mini MK3 MIDI Remote Script for Ableton Live

Tested only on Live 11 but should be compatible with Live 7, 8, 9 and 10.


## Control Ableton via the MPK Mini MK3

![MMMKIII Setup](assets/images/MMMKIII.png)

***MMMKIII*** is a ***MIDI Remote Script*** for Ableton Live that gives access to common settings of the currently selected track via **CC messages** (arm, mute, solo, volume, pan…) as well as the currently selected device (on/off, parameters, banks, lock…). Furthermore some global controls are instantly mapped as well.

Among the mapped functionality is:

*	**arm**, **solo** and **mute** the selected track
*	control **volume, pan** and **send 1-4** of the selected track
*	**toggle loop, record, play and stop**
*	**Navigate device view**
*	**Navigate session-view**
*	**Navigate arrangement-view** 
*	**Fire scenes and clips**
*	…

To make this work, 4 programs needs to be sent to the controller using the MPK Mini MK3 Program Editor.

There are 4 Programs: The first two programs BANK B is the same as the device program, this will allow you to switch quickly to the device mapping using the BANK A/B button.

### Arrangement:
![Arragenement Setup](assets/images/ARRANGEMENT%20SETUP.png)

### Session:
![image description](assets/images/SESSION%20SETUP.png)

### Mixer:
![image description](assets/images/MIXER%20SETUP.png)

### Device:
![image description](assets/images/DEVICE%20SETUP.png)



## Installation


Download the latest release zip [from here](https://github.com/SlyBouhafs/MMMKIII/releases/latest) and unzip it or clone the repository.

1.	Stop Live if it is running.
2.	In the `assets/presets/` folder, there are 4 programs, use the MPK Mini MK3 Program Editor to install each one.
3.	Add **MMMKIII** to Ableton Live's MIDI Remote Scripts

	[See Ableton’s help page regarding installing third-party remote scripts.](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts)

4.	Start Live.
5.	Enable **MMMKIII** as a Control Surface in Live

	In Live’s Preferences go to the **MIDI Sync** tab and select **MMMKIII** in the dropdown list of available Control Surfaces. As MIDI Input and Output, select your controller’s MIDI-port.
	


## License

This work is licensed under the "Simplified BSD License" / "FreeBSD License"
see License.txt



## Acknowledgement

This script is based on latest the STC 1.4.0-beta, [project’s homepage.](http://stc.wiffbi.com/)