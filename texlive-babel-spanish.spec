# revision 30295
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/spanish
# catalog-date 2013-05-04 16:20:14 +0200
# catalog-license lppl
# catalog-version 5.0j
Name:		texlive-babel-spanish
Version:	5.0j
Release:	2
Summary:	Babel support for Spanish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/spanish
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides the means to typeset Spanish text, with
the support provided by the LaTeX standard package babel. Note
that separate support is provided for those who wish to typeset
Spanish as written in Mexico.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-spanish/romanidx.sty
%{_texmfdistdir}/tex/generic/babel-spanish/spanish.ldf
%doc %{_texmfdistdir}/doc/generic/babel-spanish/spanish.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-spanish/spanish.dtx
%doc %{_texmfdistdir}/source/generic/babel-spanish/spanish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
