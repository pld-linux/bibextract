# TODO:
# - DESTDIR patch HAS to be made - during install there is 
# some substitutions done.
Summary:	Tools for extracting citation tags
Summary(pl.UTF-8):	Narzędzia do wyciągania znaczników cytowania
Name:		bibextract
Version:	1.09
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.math.utah.edu/pub/tex/bib/%{name}-%{version}.tar.bz2
# Source0-md5:	c8abaf606cdd50a7c45669babb06fcc2
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for extracting citation tags from LaTeX and .aux files and
extracting those entries from BibTeX files.

%description -l pl.UTF-8
Narzędzia do wyciągania znaczników cytowania z LaTeXa i plików .aux
oraz wyciągania tych wpisów z plików BibTeXa.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.txt *.ps
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
