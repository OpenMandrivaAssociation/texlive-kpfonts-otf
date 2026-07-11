%global tl_name kpfonts-otf
%global tl_revision 78294

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.73
Release:	%{tl_revision}.1
Summary:	OpenType versions of the kpfonts (Type1) designed by Christophe Caignaert
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/kpfonts-otf
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides OpenType versions of the Type1 Kp-fonts designed by
Christophe Caignaert. It is usable with LuaTeX or XeTeX engines only. It
consists of sixteen Text fonts (eight Serif, four Sans-Serif, four
Monotype) and six Math fonts. Serif and Sans-Serif families have small
caps available in two sizes (SmallCaps and PetitesCaps), upper and
lowercase digits, real superscripts and subscripts; ancient ligatures
(ct and st), ancient long-s and a long-tailed capital Q are available
via font features. Math fonts cover all usual symbols including AMS'; a
full list of available symbols is provided, see the 'List of glyphs'.

