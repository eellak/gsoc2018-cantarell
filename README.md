# gsoc2018-cantarell

## Adding Greek language support to the open source fonts of Cantarell

### **Links**

- [GSoC project page](https://summerofcode.withgoogle.com/organizations/4954936912117760/#6670474218569728)
- [Gist with the final report](https://gist.github.com/grautesk/a8513e1b668be03238140b2cebfe18ac)

---

## Synopsis

[Cantarell](https://github.com/madig/cantarell-fonts) is a humanist sans serif typeface optimized for on-screen reading. It was originally developed by Dave Crossland in the MA Typeface Design class of 2009 at the University of Reading using free software. Subsequently, it was licensed under an [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL) and has been the standard UI typeface for the open-source desktop environment [GNOME](https://github.com/GNOME) since version 3.0 in 2010.

The fonts have been redesigned for the [release](https://help.gnome.org/misc/release-notes/3.28/) of GNOME 3.28 in March 2018. Post-script outline quality improved significantly, spacing has been reworked and new weights have been added.

The family is currently growing to support additional writing systems. After initially applying with extending another typeface I was invited to change my project and add Monotonic and Polytonic Greek to the three Roman masters of Cantarell during [Google Summer of Code](https://summerofcode.withgoogle.com) 2018.

## Process

There is a detailed résumé of this project in a [gist](https://gist.github.com/grautesk/a8513e1b668be03238140b2cebfe18ac). [00_Process](https://github.com/eellak/gsoc2018-cantarell/tree/master/00_PROCESS) in this repository was the work in progress folder during Google Summer of Code. [01_GSoC FINAL](https://github.com/eellak/gsoc2018-cantarell/tree/master/01_GSoC%20FINAL) comprises the status on the day of the final evaluation in mid August 2018, including the [GLYPHS-file](https://github.com/eellak/gsoc2018-cantarell/tree/master/01_GSoC%20FINAL/02_GLYPHS), exported [UFOs](https://github.com/eellak/gsoc2018-cantarell/tree/master/01_GSoC%20FINAL/03_UFO) and installable [fonts](https://github.com/eellak/gsoc2018-cantarell/tree/master/01_GSoC%20FINAL/04_Fonts).

![Cantarell Greek](https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/01_GSoC%20FINAL/01_Resources/Cantarell_Specimen_20180814.jpg)

---

## Timeline

Summary of the [detailed timeline](https://github.com/eellak/gsoc2018-cantarell/blob/master/TIMELINE.md)

**14.05. – 14.06.2018**<br />
Design lowercase and uppercase: Regular

**15.06.**<br />
Phase 1 evaluation deadline

**16.06. – 12.07.**<br />
Design lowercase and uppercase: Extra Bold, Thin; Interpolation test

**13.07.**<br />
Phase 2 evaluation deadline

**14.07. – 13.08.**<br />
Add Polytonic diacritics: Thin, Regular, Extra Bold; Kerning of the masters; Interpolation of intermediate weights

**14.08.2018**<br />
Final evaluation deadline

---

## GSoC

### Mentors
- Alexios Zavras
- Emilios Theofanous | [GitHub](https://github.com/thynem) | [Twitter](https://twitter.com/emilios__)
- Irene Vlachou | [GitHub](https://github.com/irenevl) | [Twitter](https://twitter.com/irene_vlachou)


### Student
Florian Fecher | EsadType, Amiens | [GitHub](https://github.com/grautesk) | [Twitter](https://twitter.com/grautesk)


### Organization
[Open Technologies Alliance – GFOSS](https://summerofcode.withgoogle.com/organizations/4954936912117760/#6670474218569728) | [GitHub](https://github.com/eellak) | [Twitter](https://twitter.com/gfoss_en)

---

## License

The Cantarell fonts and related code are licensed under an [SIL Open Font License](https://github.com/madig/cantarell-fonts/blob/master/COPYING).
