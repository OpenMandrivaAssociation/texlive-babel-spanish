%global tl_name babel-spanish
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.0q
Release:	%{tl_revision}.1
Summary:	Babel support for Spanish
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/spanish
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides the means to typeset Spanish text, with the support
provided by the LaTeX standard package babel. Note that separate support
is provided for those who wish to typeset Spanish as written in Mexico.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-spanish
%dir %{_datadir}/texmf-dist/source/generic/babel-spanish
%dir %{_datadir}/texmf-dist/tex/generic/babel-spanish
%doc %{_datadir}/texmf-dist/doc/generic/babel-spanish/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-spanish/spanish.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-spanish/spanish.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-spanish/spanish.ins
%{_datadir}/texmf-dist/tex/generic/babel-spanish/romanidx.sty
%{_datadir}/texmf-dist/tex/generic/babel-spanish/spanish.ldf
