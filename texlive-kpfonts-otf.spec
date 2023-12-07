Name:		texlive-kpfonts-otf
Version:	68970
Release:	1
Summary:	OpenType version of the kpfonts (Type1) designed by Christophe Caignaert
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kpfonts-otf
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides OpenType versions of the Type1 Kp-fonts
designed by Christophe Caignaert. It is usable with LuaTeX or
XeTeX engines only. It consists of sixteen Text fonts (eight
Serif, four Sans-Serif, four Monotype) and five Math fonts.
Serif and Sans-Serif families have small caps available in two
sizes (SmallCaps and PetitesCaps), upper and lowercase digits,
real superscripts and subscripts; ancient ligatures (ct and
st), ancient long-s and a long-tailed capital Q are available
via font features. Math fonts cover all usual symbols including
AMS'; a full list of available symbols is provided, see the
'List of glyphs'.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/kpfonts-otf
%{_texmfdistdir}/fonts/opentype/public/kpfonts-otf
%doc %{_texmfdistdir}/doc/fonts/kpfonts-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
