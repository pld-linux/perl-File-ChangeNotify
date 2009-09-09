#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ChangeNotify
Summary:	File::ChangeNotify - Watch for changes to files, cross-platform style
#Summary(pl.UTF-8):
Name:		perl-File-ChangeNotify
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1459d99d91420d14d75bb5d000aa3aa2
URL:		http://search.cpan.org/dist/File-ChangeNotify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Params::Validate) >= 0.08
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl-Class-MOP
BuildRequires:	perl-Moose
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an API for creating a File::ChangeNotify::Watcher
subclass that will work on your platform.

Most of the documentation for this distro is in
File::ChangeNotify::Watcher.

# %description -l pl.UTF-8

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
%{perl_vendorlib}/File/ChangeNotify
%{_mandir}/man3/*
