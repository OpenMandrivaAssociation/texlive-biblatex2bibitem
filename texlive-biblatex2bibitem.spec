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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some journals accept the reference list only as \bibitems. If you use
BibTeX, there is no problem: just paste the content of the .bbl file
into your document. However, there was no out-of-the-box way to do the
same for biblatex, and you had to struggle with searching appropriate
.bst files, or formatting your reference list by hand, or something like
that. Using the workaround provided by this package solves the problem.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem
%dir %{_datadir}/texmf-dist/tex/latex/biblatex2bibitem
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref-result.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref-result.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe-result.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe-result.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-new-result.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex2bibitem/biblatex2bibitem-new.pdf
%{_datadir}/texmf-dist/tex/latex/biblatex2bibitem/biblatex2bibitem.sty
