# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/frankenstein
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-frankenstein
Version:	20080819
Release:	2
Summary:	A collection of LaTeX packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frankenstein
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frankenstein.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frankenstein.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frankenstein.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Frankenstein is a bundle of LaTeX packages serving various
purposes and a BibTeX bibliography style. Descriptions are
given under the individual packages: abbrevs, achicago package,
achicago bibstyle, attrib, blkcntrl, compsci, dialogue, lips,
moredefs, newclude, slemph, titles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/frankenstein/frankenstein.bib
%{_texmfdistdir}/bibtex/bst/frankenstein/achicago.bst
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.cfg
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.stq
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.sty
%{_texmfdistdir}/tex/latex/frankenstein/achicago.stq
%{_texmfdistdir}/tex/latex/frankenstein/achicago.sty
%{_texmfdistdir}/tex/latex/frankenstein/allocate.sto
%{_texmfdistdir}/tex/latex/frankenstein/attrib.stq
%{_texmfdistdir}/tex/latex/frankenstein/attrib.sty
%{_texmfdistdir}/tex/latex/frankenstein/blkcntrl.stq
%{_texmfdistdir}/tex/latex/frankenstein/blkcntrl.sty
%{_texmfdistdir}/tex/latex/frankenstein/compsci.cfg
%{_texmfdistdir}/tex/latex/frankenstein/compsci.stq
%{_texmfdistdir}/tex/latex/frankenstein/compsci.sty
%{_texmfdistdir}/tex/latex/frankenstein/dialogue.stq
%{_texmfdistdir}/tex/latex/frankenstein/dialogue.sty
%{_texmfdistdir}/tex/latex/frankenstein/lips.stq
%{_texmfdistdir}/tex/latex/frankenstein/lips.sty
%{_texmfdistdir}/tex/latex/frankenstein/moredefs.stq
%{_texmfdistdir}/tex/latex/frankenstein/moredefs.sty
%{_texmfdistdir}/tex/latex/frankenstein/newclude.stq
%{_texmfdistdir}/tex/latex/frankenstein/newclude.sty
%{_texmfdistdir}/tex/latex/frankenstein/simple.sto
%{_texmfdistdir}/tex/latex/frankenstein/slemph.cfg
%{_texmfdistdir}/tex/latex/frankenstein/slemph.stq
%{_texmfdistdir}/tex/latex/frankenstein/slemph.sty
%{_texmfdistdir}/tex/latex/frankenstein/tag.sto
%{_texmfdistdir}/tex/latex/frankenstein/titles.cfg
%{_texmfdistdir}/tex/latex/frankenstein/titles.stq
%{_texmfdistdir}/tex/latex/frankenstein/titles.sty
%doc %{_texmfdistdir}/doc/latex/frankenstein/ChangeLog
%doc %{_texmfdistdir}/doc/latex/frankenstein/Frankenfile
%doc %{_texmfdistdir}/doc/latex/frankenstein/INSTALL
%doc %{_texmfdistdir}/doc/latex/frankenstein/README
%doc %{_texmfdistdir}/doc/latex/frankenstein/abbrevs.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/abbrevs.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.ver
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago.bsq
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/achicago.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/attrib.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/attrib.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/blkcntrl.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/blkcntrl.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/compsci.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/compsci.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/dialogue.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/dialogue.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/lips.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/lips.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/moredefs.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/moredefs.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/newclude.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/newclude.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/slemph.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/slemph.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/titles.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/titles.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/README-unsupported
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.cfg
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.ins
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.sty
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.ins
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.sty
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex-test.tex
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.ins
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.pdf
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.sty
%doc %{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.tex
#- source
%doc %{_texmfdistdir}/source/latex/frankenstein/Makefile
%doc %{_texmfdistdir}/source/latex/frankenstein/abbrevs.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/achicago-bst.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/achicago.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/attrib.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/blkcntrl.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/compsci.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/dialogue.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/lips.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/moredefs.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/newclude.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/slemph.ins
%doc %{_texmfdistdir}/source/latex/frankenstein/titles.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080819-2
+ Revision: 752095
- Rebuild to reduce used resources

* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080819-1
+ Revision: 729016
- texlive-frankenstein
- texlive-frankenstein
- texlive-frankenstein
- texlive-frankenstein
- texlive-frankenstein

