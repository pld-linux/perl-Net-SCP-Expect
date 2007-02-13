#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SCP-Expect
Summary:	Net::SCP::Expect - Wrapper for scp that allows passwords via Expect
Summary(pl.UTF-8):	Net::SCP::Expect - wrapper dla scp umożliwiający podawanie haseł przez Expect
Name:		perl-Net-SCP-Expect
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed57459ab1511bed85479bdcb18cc67a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Expect >= 1.14
BuildRequires:	perl-Term-ReadPassword >= 0.01
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is simply a wrapper around the scp call. The primary
difference between this module and Net::SCP is that you may send
a password programmatically, instead of being forced to deal with
interactive sessions.

%description -l pl.UTF-8
Ten moduł jest prostym wrapperem dla wywołań scp. Główna różnica
między tym modułem a Net::SCP jest taka, że można programowo wysłać
hasło zamiast być zmuszonym do obsługi interaktywnych sesji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Net/*/*.pm
%{_mandir}/man3/*
