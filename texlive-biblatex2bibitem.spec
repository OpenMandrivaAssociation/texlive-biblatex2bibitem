%global tl_name biblatex2bibitem
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Convert BibLaTeX-generated bibliography to bibitems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex2bibitem
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex2bibitem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex2bibitem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some journals accept the reference list only as \bibitems. If you use
BibTeX, there is no problem: just paste the content of the .bbl file
into your document. However, there was no out-of-the-box way to do the
same for biblatex, and you had to struggle with searching appropriate
.bst files, or formatting your reference list by hand, or something like
that. Using the workaround provided by this package solves the problem.

