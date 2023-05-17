# The Ultimate Akai MPK Mini MK3 MIDI Remote Script for Ableton Live

Tested only on Live 11 but should be compatible with Live 7, 8, 9 and 10.

## Control Ableton via the MPK Mini MK3

![MMMKIII Setup](assets/images/MMMKIII.png)

Experience enhanced control over Ableton Live with ***MMMKIII***, a powerful ***MIDI Remote Script*** designed to provide convenient access to common track settings and device parameters while effortlessly navigating through device view, session view, and arrangement view.


***MMMKIII*** is a ***MIDI Remote Script*** for Ableton Live that gives access to common settings of the currently selected track via **CC messages** (arm, mute, solo, volume, pan…) as well as the currently selected device (on/off, parameters, banks, lock…).

Among the mapped functionality is:

*	**Arm**, **solo** and **mute** the selected track
*	Control **volume, pan** and **send 1-4** of the selected track
*	**Toggle loop, record, play and stop**
*	**Navigate device view**
*	**Navigate session-view**
*	**Navigate arrangement-view** 
*	**Fire scenes and clips**
*	…

In order to ensure functionality, I created four programs that need to be loaded into the controller through the MPK Mini MK3 Program Editor.


The *BANK B* of the first two programs mirrors the device program, enabling quick switching between device mappings using the BANK A/B button.

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

1.	Make sure that Live isn't running.
2.	In the `assets/presets/` folder, there are 4 programs, use the MPK Mini MK3 Program Editor to load each one.
3.	Add **MMMKIII** to Ableton Live's MIDI Remote Scripts folder.

	[See Ableton’s help page regarding installing third-party remote scripts.](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts)

4.	Start Live.
5.	Enable **MMMKIII** as a Control Surface in Live

	In Live’s Preferences go to the **MIDI Sync** tab and select **MMMKIII** in the dropdown list of available Control Surfaces. For the MIDI Input and Output, select your controller’s MIDI-port.
	

## License

This work is licensed under the "Simplified BSD License" / "FreeBSD License"
see License.txt


## Acknowledgement

This script is based on latest the STC 1.4.0-beta, [project’s homepage.](http://stc.wiffbi.com/)