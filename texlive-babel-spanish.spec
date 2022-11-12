Name:		texlive-babel-spanish
Version:	59367
Release:	1
Summary:	Babel support for Spanish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/spanish
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.r59367.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.doc.r59367.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-spanish.source.r59367.tar.xz
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
%{_texmfdistdir}/tex/generic/babel-spanish
%doc %{_texmfdistdir}/doc/generic/babel-spanish
#- source
%doc %{_texmfdistdir}/source/generic/babel-spanish

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
