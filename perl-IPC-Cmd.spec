%{?scl:%scl_package perl-IPC-Cmd}

# Use IPC::Run
%if ! (0%{?scl:1})
%bcond_without perl_IPC_Cmd_enables_IPC_Run
%endif

Name:           %{?scl_prefix}perl-IPC-Cmd
# Epoch to compete with perl.spec
Epoch:          2
Version:        1.04
Release:        3%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IPC-Cmd
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
# Replace ExtUtils::MakeMaker dependency with ExtUtils::MM::Utils.
# This enables not to require perl-devel. Bug #1129443
Patch0:         IPC-Cmd-0.96-Replace-EU-MM-dependency-with-EU-MM-Utils.patch
BuildArch:      noarch
# Build:
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MM::Utils)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
%if %{with perl_IPC_Cmd_enables_IPC_Run} && !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(IPC::Run) >= 0.55
%endif
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::Load::Conditional) >= 0.66
BuildRequires:  %{?scl_prefix}perl(Params::Check) >= 0.20
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
BuildRequires:  %{?scl_prefix}perl(Time::HiRes)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
# output.pl/IO::Handle not used
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Dependencies:
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(ExtUtils::MM::Utils)
Requires:       %{?scl_prefix}perl(FileHandle)
Requires:       %{?scl_prefix}perl(IO::Handle)
Requires:       %{?scl_prefix}perl(IO::Select)
Requires:       %{?scl_prefix}perl(IPC::Open3)
%if %{with perl_IPC_Cmd_enables_IPC_Run}
Requires:       %{?scl_prefix}perl(IPC::Run) >= 0.55
%endif
Requires:       %{?scl_prefix}perl(Module::Load::Conditional) >= 0.66
Requires:       %{?scl_prefix}perl(Params::Check) >= 0.20
Requires:       %{?scl_prefix}perl(POSIX)
Requires:       %{?scl_prefix}perl(Socket)
Requires:       %{?scl_prefix}perl(Time::HiRes)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Module::Load::Conditional\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Params::Check\\)$

%description
IPC::Cmd allows you to run commands platform independently, interactively
if desired, but have them still work.

%prep
%setup -q -n IPC-Cmd-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Cmd.3*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.04-3
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Pisar <ppisar@redhat.com> - 2:1.04-1
- 1.04 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.02-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.02-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.02-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.02-2
- Perl 5.28 rebuild

* Thu May 03 2018 Petr Pisar <ppisar@redhat.com> - 2:1.02-1
- 1.02 bump

* Thu Feb 15 2018 Petr Pisar <ppisar@redhat.com> - 2:1.00-1
- 1.00 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.98-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.98-2
- Perl 5.26 rebuild

* Sun May 14 2017 Paul Howarth <paul@city-fan.org> - 1:0.98-1
- Update to 0.98
  - Added wait_loop_callback for run_forked()
  - Only search in curdir in can_run() when on Win32 (CPAN RT#105601)
- Drop redundant Group: tag

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.96-3
- Don't BR: perl(IPC::Run) when bootstrapping

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Paul Howarth <paul@city-fan.org> - 1:0.96-1
- Update to 0.96
  - Require Module::Load::Conditional 0.66 to resolve CVE-2016-1238
    (avoid loading optional modules from default .)
- Update patch for use of ExtUtils::MM::Utils
- Simplify find command using -delete

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.94-4
- Perl 5.24 rebuild

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 1:0.94-3
- Replace ExtUtils::MakeMaker dependency with ExtUtils::MM::Utils (bug #1129443)

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> - 1:0.94-2
- Weaken dependency on IPC::Run (bug #1307195)

* Sat Feb 13 2016 Paul Howarth <paul@city-fan.org> - 1:0.94-1
- 0.94 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.92-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.92-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.92-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.92-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.92-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Petr Pisar <ppisar@redhat.com> - 1:0.92-1
- 0.92 bump

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 1:0.90-1
- 0.90 bump

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 1:0.86-1
- 0.86 bump

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 1:0.84-1
- 0.84 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.82-2
- Perl 5.18 rebuild

* Mon Jul 08 2013 Petr Pisar <ppisar@redhat.com> - 1:0.82-1
- 0.82 bump

* Mon May 20 2013 Petr Pisar <ppisar@redhat.com> - 1:0.80-3
- Remove unneeded dependency on Config

* Thu Mar 14 2013 Petr Pisar <ppisar@redhat.com> - 1:0.80-2
- Set epoch to compete with core module from perl.spec

* Mon Mar 04 2013 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Fri Feb 08 2013 Petr Pisar <ppisar@redhat.com> 0.78-1
- Specfile autogenerated by cpanspec 1.78.
