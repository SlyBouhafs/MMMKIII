from .MIDI import *  # import MIDI status codes

""" settings which MIDI-notes and CCs trigger which functionality """


# debug_mode: whether the log-function should output to logfile
debug_mode = False

"""
	"<setting>": Note (<MIDI note#> [, <MIDI channel>])
	"<setting>": CC (<MIDI CC#> [, <mapping mode> [, <MIDI channel>]])
	
	if <mapping mode> is ommitted, it is assumed MIDI.RELATIVE_TWO_COMPLIMENT
		other modes are: ABSOLUTE, RELATIVE_BINARY_OFFSET, RELATIVE_SIGNED_BIT, RELATIVE_SIGNED_BIT2 
		see the documentation of your device which type MIDI CC it sends
	
	if <MIDI channel> is ommitted, it is assumed MIDI.DEFAULT_CHANNEL
		the DEFAULT_CHANNEL channel is set to 0 (ie. channel 1 if you count from 1-16)
		MIDI channels are zero-indexed, ie. you count from 0 to 15
		you can change DEFAULT_CHANNEL in MIDI.py
	
	
	
	
	Some examples for setting up your own mappings:
	
	
	- Mapping "arm" to Note #64 on MIDI channel 4 (if you count channels 1-16):
		
		"arm": Note(64, 3),
	
	
	- Mapping "pan" to an encoder with CC #23 on MIDI channel 8 (if you count channels 1-16):
	  Note: encoders usually send RELATIVE values - in this example in RELATIVE_TWO_COMPLIMENT format

		"pan": CC(23, RELATIVE_TWO_COMPLIMENT, 7),
	
	
	- Mapping "volume" to a fader with CC #7 on MIDI channel 2 (if you count channels 1-16):
	  Note: faders usually send ABSOLUTE values

		"arm": CC(7, ABSOLUTE, 1),
	
	
	- Mapping sends
	  Sends are mapped the same way as other controls, only that you can provide multiple CC()-defintions
	  in a so called "tuple" (that is basically a list). The first CC maps to "Send 1", the second CC 
	  to "Send 2", etc.
	  
	  A tuple is defined like so:
	  
	  (<element>, <element>, <element>)
	  
	  A basic example, mapping knobs with CC #12-19 on MIDI channel 16 (if you count channels 1-16):
	  Note: knobs usually send ABSOLUTE values
	  
		"sends": (
			CC(12, ABSOLUTE, 15),
			CC(13, ABSOLUTE, 15),
			CC(14, ABSOLUTE, 15),
			CC(15, ABSOLUTE, 15),
			CC(16, ABSOLUTE, 15),
			CC(17, ABSOLUTE, 15),
			CC(18, ABSOLUTE, 15),
			CC(19, ABSOLUTE, 15),
		),
	
	
	
	
	
	
	- ADVANCED FEATURE: binding multiple MIDI messages to the same control
	  
	  This is mainly useful to support multiple MIDI bindings in STC by default.
	  Note that e.g. volume is mapped by default to MIDI CC #22 as RELATIVE_TWO_COMPLIMENT and at the 
	  same time to MIDI CC #7 as ABSOLUTE.
	  See documentation here: http://stc.wiffbi.com/midi-implementation-chart/
	  
	  Binding multiple MIDI messages to one control is done by using a tuple of CC/Note-commands. 
	  It is actually the same as defining controls for sends. Looking at the default defintion
	  for "volume"
	
		"volume": (CC(22), CC(7, ABSOLUTE)),
	
	  and adding some white-space/newlines
	
		"volume": (
			CC(22),
			CC(7, ABSOLUTE)
		),
	  
	  reveals, that is looks similar to the definition of sends described earlier.
	  
	  BONUS: even a single send-control can be mapped to multiple MIDI-commands. As sends are defined as 
	  a tuple of CC-commands, we can instead of a single CC-command use a tuple of CC-commands. This 
	  results in a tuple of tuples of CC-commands.
	  
	  The default definition of sends are such a construct:
	
		"sends": (
			(CC(24), CC(12, ABSOLUTE)),
			(CC(25), CC(13, ABSOLUTE)),
			(CC(26), CC(14, ABSOLUTE)),
			(CC(27), CC(15, ABSOLUTE)),
			(CC(28), CC(16, ABSOLUTE)),
			(CC(29), CC(17, ABSOLUTE)),
			(CC(30), CC(18, ABSOLUTE)),
			(CC(31), CC(19, ABSOLUTE)),
		),
	  
	  "Send 1" is mapped to CC #24 in RELATIVE_TWO_COMPLIMENT on the DEFAULT_CHANNEL as well as to 
	           CC #12 in ABSOLUTE on the DEFAULT_CHANNEL
	  "Send 2" is mapped to CC #25 in RELATIVE_TWO_COMPLIMENT on the DEFAULT_CHANNEL as well as to 
	           CC #14 in ABSOLUTE on the DEFAULT_CHANNEL
	  ...
"""

# these values are only used if you map tempo-control to an absolute controller
tempo_min = 60
tempo_max = 187

volume_default = 0.55  # this value is -12db (trial-and-error to set as there is no mapping function available)

scrub_increment = 2  # scrubs by ticks

auto_select_playing_clip = False

# this feature is currently only planned
# reset_device_bank = False # Reset device-bank to 0 when selecting another device

auto_arm = (
    True  # default behaviour for auto-arming a track on selection, either False or True
)
has_midi_loopback = False  # auto-arm on selection (including when selecting via mouse) usually only works with the STC.app on Mac, which provides MIDI-loopback-functionality. If you use STC.app, set has_midi_loopback = True, else set has_midi_loopback = False. If set to False, auto-arm on selection works even without STC.app, but only if you use STC-MIDI Remote Script and MIDI to select a track (so if you select a track via mouse, it will not be automatically armed)

# either dict or False
device_bestof = False
# device_bestof = {
# 	"Impulse": (4,3,2,1,8,7,6,5),
# 	"Looper": (2,1,0),
# }

# either a list of Device-names or integer or Boolean (True will select first device)
# automatically selects the device if available when switched to the track
# to select last device set to a big int - at least as big as max number of devices per track, e.g. 255
auto_select_device = False
# auto_select_device = ["Looper", "Impulse", "Simpler"]


# clip_trigger_quantization_steps reflects the quantization setting in the transport bar.
# 0: None
# 1: 8 Bars
# 2: 4 Bars
# 3: 2 Bars
# 4: 1 Bar
# 5: 1/2
# 6: 1/2T
# 7: 1/4
# 8: 1/4T
# 9: 1/8
# 10: 1/8T
# 11: 1/16
# 12: 1/16T
# 13: 1/32

# define which quantization steps should be stepped through - use range(14) to step through all available
clip_trigger_quantization_steps = [0, 1, 2, 3, 4, 5, 7, 9, 11, 13]

# to use all quantization steps, remove the # at the beginning of the following line
# clip_trigger_quantization_steps = range(14)


# midi_recording_quantization_steps reflects the current selection of the Edit->Record Quantization menu.
# 0: None
# 1: 1/4
# 2: 1/8
# 3: 1/8T
# 4: 1/8 + 1/8T
# 5: 1/16
# 6: 1/16T
# 7: 1/16 + 1/16T
# 8: 1/32

# define which quantization steps should be stepped through - use range(9) to step through all available
midi_recording_quantization_steps = [0, 1, 2, 5, 8]

# to use all quantization steps, remove the # at the beginning of the following line
# midi_recording_quantization_steps = range(9)


midi_mapping = {
    #
    # Active commands
    #
    #
    # Arrangement
    #
    "play_pause": CC(2, ABSOLUTE),
    "stop_playing": CC(3, ABSOLUTE),
    "record": CC(4, ABSOLUTE),
    "loop": CC(5, ABSOLUTE),
    "scrub_rewind": CC(7, ABSOLUTE),
    "scrub_forward": CC(8, ABSOLUTE),
    "prev_track": (CC(6, ABSOLUTE), CC(14, ABSOLUTE), CC(22, ABSOLUTE)),
    "next_track": (CC(9, ABSOLUTE), CC(17, ABSOLUTE), CC(25, ABSOLUTE)),
    #
    # Sessions
    #
    "toggle_selected_clip": CC(10, ABSOLUTE),
    "fire_or_stop_selected_scene": CC(11, ABSOLUTE),
    # "overdub": CC(12, ABSOLUTE),
    "session_record": CC(12, ABSOLUTE),
    "delete_selected_clip": CC(13, ABSOLUTE),
    "prev_scene": CC(15, ABSOLUTE),
    "next_scene": CC(16, ABSOLUTE),
    #
    # Mixer
    #
    "solo": CC(18, ABSOLUTE),
    "mute": CC(19, ABSOLUTE),
    "arm": CC(20, ABSOLUTE),
    "toggle_track_fold": CC(21, ABSOLUTE),
    "first_track": CC(23, ABSOLUTE),
    "last_track": CC(24, ABSOLUTE),
    "volume": CC(58, RELATIVE_TWO_COMPLIMENT, 0),
    "pan": CC(59, RELATIVE_TWO_COMPLIMENT, 0),
    "sends": (
        CC(60, RELATIVE_TWO_COMPLIMENT, 0),
        CC(61, RELATIVE_TWO_COMPLIMENT, 0),
        CC(62, RELATIVE_TWO_COMPLIMENT, 0),
        CC(63, RELATIVE_TWO_COMPLIMENT, 0),
    ),
    "cue_volume": CC(64, RELATIVE_TWO_COMPLIMENT, 0),
    "master_volume": CC(65, RELATIVE_TWO_COMPLIMENT, 0),
    #
    # Device
    #
    "toggle_lock_to_device": CC(34, ABSOLUTE),
    "toggle_detail_device": CC(35, ABSOLUTE),
    # "select_instrument": CC(35, ABSOLUTE),
    "device_on_off": CC(36, ABSOLUTE),
    "collapse_device": CC(37, ABSOLUTE),
    "prev_device": CC(38, ABSOLUTE),
    "next_device_bank": CC(40, ABSOLUTE),
    "next_device": CC(41, ABSOLUTE),
    "prev_device_bank": CC(39, ABSOLUTE),
    "device_params": (
        CC(70, RELATIVE_TWO_COMPLIMENT, 0),
        CC(71, RELATIVE_TWO_COMPLIMENT, 0),
        CC(72, RELATIVE_TWO_COMPLIMENT, 0),
        CC(73, RELATIVE_TWO_COMPLIMENT, 0),
        CC(74, RELATIVE_TWO_COMPLIMENT, 0),
        CC(75, RELATIVE_TWO_COMPLIMENT, 0),
        CC(76, RELATIVE_TWO_COMPLIMENT, 0),
        CC(77, RELATIVE_TWO_COMPLIMENT, 0),
    ),
    #
    # Inactive commands
    #
    #
    # track controls
    #
    # "arm": CC(0),
    # "arm_exclusive": Note(3),
    # "arm_kill": Note(10),
    # "arm_flip": Note(115),
    # "solo": CC(1),
    # "solo_exclusive": Note(4),
    # "solo_kill": Note(7),
    # "solo_flip": Note(116),
    # "mute": CC(29),
    # "mute_exclusive": Note(5),
    # "mute_kill": Note(8),
    # "mute_flip": Note(9),
    # "switch_monitoring": Note(6),
    # "input_rotate": (Note(60), CC(60, ABSOLUTE)),
    # "input_sub_rotate": (Note(61), CC(61, ABSOLUTE)),
    # "input_none": Note(62),
    # "output_rotate": (Note(63), CC(63, ABSOLUTE)),
    # "output_sub_rotate": (Note(64), CC(64, ABSOLUTE)),
    # "output_none": Note(65),
    # "volume": CC(70, RELATIVE_TWO_COMPLIMENT, 0),
    # "pan": CC(71, RELATIVE_TWO_COMPLIMENT, 0),
    # "reset_volume": Note(22),
    # "reset_pan": Note(23),
    # "sends": (
    #     (CC(24), CC(12, ABSOLUTE)),
    #     (CC(25), CC(13, ABSOLUTE)),
    #     (CC(26), CC(14, ABSOLUTE)),
    #     (CC(27), CC(15, ABSOLUTE)),
    #     (CC(28), CC(16, ABSOLUTE)),
    #     (CC(29), CC(17, ABSOLUTE)),
    #     (CC(30), CC(18, ABSOLUTE)),
    #     (CC(31), CC(19, ABSOLUTE)),
    # ),
    # reset_sends is deprecated
    # "reset_sends": (
    # 	Note(24),
    # 	Note(25),
    # 	Note(26),
    # 	Note(27),
    # 	Note(28),
    # 	Note(29),
    # 	Note(30),
    # 	Note(31),
    # ),
    #
    # session controls
    #
    # "scroll_scenes": (CC(84), CC(9, ABSOLUTE)),
    # "scroll_tracks": (CC(85), CC(11, ABSOLUTE)),
    # "select_scene": CC(2, ABSOLUTE),
    # "select_track": CC(8, ABSOLUTE),
    # "toggle_auto_arm": Note(11),
    # "prev_scene": CC(22, ABSOLUTE),
    # "next_scene": CC(23 , ABSOLUTE),
    # "prev_track": CC(20, ABSOLUTE),
    # "next_track": CC(21, ABSOLUTE),
    # "play_selected_scene": CC(44, ABSOLUTE),
    # "play_next_scene": Note(40),
    # 	"play_prev_scene": Note(36),
    # "first_scene": Note(37),
    # "last_scene": Note(39),
    # "first_track": Note(46),
    # "last_track": Note(47),
    # "play_selected_clip": (
    #     Note(43),
    #     NoteOff(43),
    # ),  # listen to "Note Off" as well, to support clip-launch mode "Gate"
    # "toggle_selected_clip": CC(43, ABSOLUTE),
    # "play_next_clip": Note(45),
    # "play_prev_clip": Note(41),
    # "play_next_available_clip": Note(44),
    # "play_prev_available_clip": Note(42),
    # "stop_all_clips": Note(49),
    # "stop_selected_track": CC(48, ABSOLUTE),
    # "select_playing_clip": Note(50),  # highlights clipslot with currently playing clip
    # "toggle_auto_select_playing_clip": Note(51),
    # "toggle_mute_selected_clip": Note(50), # does not do anything
    # "toggle_track_collapsed": (CC(79), Note(94)),
    # "toggle_track_fold": CC(73),
    # "assign_crossfade": CC(31, ABSOLUTE),
    # "toggle_crossfade_a": Note(91),
    # "toggle_crossfade_b": Note(92),
    # "assign_crossfade_none": Note(93),
    # "crossfader": (CC(75), CC(76, ABSOLUTE)),
    # "cue_volume": CC(77, RELATIVE_TWO_COMPLIMENT, 0),
    # "master_volume": (CC(80), CC(81, ABSOLUTE)),
    #
    # global controls
    #
    # "tempo": (CC(86), CC(20, ABSOLUTE)),
    # "tap_tempo": Note(86),  # attention: Live 8 only!
    # "tempo_increase": Note(87),
    # "tempo_decrease": Note(88),
    # "nudge_down": (Note(110), NoteOff(110)),
    # "nudge_up": (Note(111), NoteOff(111)),
    # "groove_amount": CC(120),
    # "play_stop": CC(16, ABSOLUTE),
    # "play_pause": Note(21),
    # "play_selection": Note(24),
    # "stop_playing": CC(17),
    # "start_playing": CC(16),
    # "continue_playing": Note(29),
    # global arrangement scrubbing
    # "scrub_by": CC(90),
    # "scrub_forward": CC(19, ABSOLUTE),
    # "scrub_rewind": CC(18, ABSOLUTE),
    # "undo": Note(80),
    # "redo": Note(81),
    # "loop": CC(20),
    # "loop_move": CC(87),
    # "loop_lb_move": CC(88),
    # "loop_rb_move": CC(89),
    # "metronome": Note(12),
    # "back_to_arranger": Note(13),
    # "overdub": Note(14),
    # "disable_overdub": Note(15),
    # "record": CC(17, ABSOLUTE),
    # "punch_in": Note(16),
    # "punch_out": Note(17),
    # quantization control
    # steps through list of quantizations - see top for clip_trigger_quantization_steps
    # "clip_trigger_quantization": (CC(49), CC(51, ABSOLUTE), Note(25)),
    # steps through list of quantizations - see top for midi_recording_quantization_steps
    # "midi_recording_quantization": (CC(50), CC(52, ABSOLUTE), Note(26)),
    #
    # device control
    #
    # "scroll_devices": CC(32),
    # "select_instrument": CC(51, ABSOLUTE),
    # "prev_device": CC(24, ABSOLUTE),
    # "next_device": CC(27, ABSOLUTE),
    # "prev_device_bank": CC(25, ABSOLUTE),
    # "next_device_bank": CC(26, ABSOLUTE),
    # "reset_device_bank": Note(70),
    # "device_on_off": CC(69),
    # "device_params": (
    #     CC(70, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(71, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(72, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(73, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(74, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(75, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(76, RELATIVE_TWO_COMPLIMENT, 0),
    #     CC(77, RELATIVE_TWO_COMPLIMENT, 0),
    # ),
    # "reset_device_params": (
    #     Note(52),
    #     Note(53),
    #     Note(54),
    #     Note(55),
    #     Note(56),
    #     Note(57),
    #     Note(58),
    #     Note(59),
    # ),
    # "lock_to_selected_device": Note(112),
    # "unlock_from_device": Note(113),
    # "toggle_lock_to_device": CC(114),
    # "toggle_browser": Note(74),
    # "toggle_session_arranger": Note(75),
    # "toggle_detail": Note(76),
    # "toggle_detail_clip_device": Note(77),
    # "toggle_detail_clip": Note(78),
    # "toggle_detail_device": Note(79),
    #
    # Live 9
    #
    # "stop_all_clips_immediately": CC(127),
    # "create_scene_at": CC(<INT>, ABSOLUTE),# depending on value
    # "create_scene_before": Note(95),
    # "create_scene_after": Note(96),
    # "duplicate_scene": CC(<INT>, ABSOLUTE),# depending on value
    # "duplicate_selected_scene": Note(97),
    # "capture_scene": Note(98),
    # "capture_scene_except_selected": Note(99),
    # "delete_scene": CC(<INT>, ABSOLUTE), # depending on value
    # "delete_selected_scene": Note(100),
    # "duplicate_track": CC(<INT>, ABSOLUTE), # depending on value
    # "duplicate_selected_track": Note(101),
    # "create_midi_track_at": CC(<INT>, ABSOLUTE), # depending on value
    # "create_midi_track_after": Note(102),
    # "create_midi_track_before": Note(),
    # "create_audio_track_at": CC(<INT>, ABSOLUTE), # depending on value
    # "create_audio_track_after": Note(103),
    # "create_audio_track_before": Note(),
    # "create_return_track": Note(104),
    # "delete_track": CC(<INT>, ABSOLUTE), # depending on value
    # "delete_selected_track": Note(105),
    # "delete_device": CC(<INT>, ABSOLUTE), # depending on value
    # "delete_selected_device": Note(106),
    # "duplicate_clip_slot": CC(<INT>, ABSOLUTE), # depending on value
    # "duplicate_selected_clip_slot": Note(107),
    # "delete_clip": CC(<INT>, ABSOLUTE), # depending on value
    # "delete_selected_clip": Note(108),
    # "re_enable_automation": Note(109),
    # "arrangement_overdub": CC(117),
    # "session_automation_record": Note(118),
}
