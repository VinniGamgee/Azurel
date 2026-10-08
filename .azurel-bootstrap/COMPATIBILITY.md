# Azurel: Torzu compatibility experiment

Baseline: markprice4675/torzu, commit `6ead429195ef12f35a5818eba6d76f54d5421cec`.
The main branch preserves this emulation source. Android packaging uses the
Azurel label and `app.azurel.emu` application ID, so it can coexist with the baseline APK.
Existing saves/settings must be imported using the application's UI.

## Experimental branch: compat/totk-1.4.x

Targets: The Legend of Zelda: Tears of the Kingdom, Nintendo Switch updates
1.4.2 and 1.4.3. These are test targets, not a claim of validated compatibility.

Backport source: Eden commit
`a3ef2cc1838a007a2f424e88212aa6f1eb93eab3`,
"[audio_core/hid] Audio REV12+15 support + HID fixes (#2719)".
Original authors: sahyno1996, Zephyron and Shinmegumi. Upstream credits LotP
(Ryubing) and Zephyron (Citron) for research and implementation.
All original copyright and license notices are retained.

Eden's v0.0.4-rc1 release notes explicitly associate audio REV12/REV15 and HID
support with running TOTK 1.4.2:
https://git.eden-emu.dev/eden-emu/eden/releases/tag/v0.0.4-rc1
The same source does not establish TOTK 1.4.3 compatibility.

Scope: audio revision negotiation and input formats, HID shared-memory format
and counters, and newer application/service commands. Some service commands
remain stubs, and the upstream commit describes REV15 support as partial.
Torzu-specific adaptations resolve revision 13 -> 15 and missing NS declarations.
The REV15 voice parser also preserves the documented padding before src_quality
and checks its size and offset at compile time.

No changes to video_core, shader_recompiler, GPU drivers or graphics defaults.
CI checks the video_core and shader_recompiler Git tree hashes against Torzu.
That check proves source preservation, not rendering correctness on a device.

## Device validation still required

Use the same device, driver, graphics settings, save and location as the working
Torzu baseline. Test updates 1.4.2 and 1.4.3 separately, initially without mods.
For each: check boot, save loading, input, audio, and grass while walking and
turning the camera in the affected area. Record the game version, APK source
commit and emulator log. A successful APK build alone is not a game test.
