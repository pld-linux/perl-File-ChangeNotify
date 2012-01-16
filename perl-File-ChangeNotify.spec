#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ChangeNotify
Summary:	File::ChangeNotify - Watch for changes to files, cross-platform style
Summary(pl.UTF-8):	File::ChangeNotify - Obserwuje modyfikację plików
Name:		perl-File-ChangeNotify
Version:	0.20
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9bb68f6e149436ace7cb13c8f9cdb6bd
URL:		http://search.cpan.org/dist/File-ChangeNotify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Params::Validate) >= 0.08
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl-Class-MOP
BuildRequires:	perl-Moose
# not in PLD, yet
#BuildRequires:	perl-Test-Without-Module
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an API for creating a File::ChangeNotify::Watcher
subclass that will work on your platform.

Most of the documentation for this distro is in
File::ChangeNotify::Watcher.

%description -l pl.UTF-8
Moduł ten dostarcza API do tworzenia podklasy
File::ChangeNotify::Watcher która może pracować na Twojej platformie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%ifnos bsd
# BSD-specific watcher
rm $RPM_BUILD_ROOT%{perl_vendorlib}/File/ChangeNotify/Watcher/KQueue.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/File::ChangeNotify::Watcher::KQueue.3pm*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
%{perl_vendorlib}/File/ChangeNotify
%{_mandir}/man3/*
