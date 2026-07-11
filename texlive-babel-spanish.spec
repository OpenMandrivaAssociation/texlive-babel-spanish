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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides the means to typeset Spanish text, with the support
provided by the LaTeX standard package babel. Note that separate support
is provided for those who wish to typeset Spanish as written in Mexico.

