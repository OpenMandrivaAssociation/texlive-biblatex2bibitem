Name:		texlive-biblatex2bibitem
Version:	67201
Release:	1
Summary:	Convert BibLaTeX-generated bibliography to bibitems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex2bibitem
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex2bibitem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex2bibitem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Some journals accept the reference list only as \bibitems. If
you use BibTeX, there is no problem: just paste the content of
the .bbl file into your document. However, there was no
out-of-the-box way to do the same for biblatex, and you had to
struggle with searching appropriate .bst files, or formatting
your reference list by hand, or something like that. Using the
workaround provided by this package solves the problem.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex2bibitem
%doc %{_texmfdistdir}/doc/latex/biblatex2bibitem

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
