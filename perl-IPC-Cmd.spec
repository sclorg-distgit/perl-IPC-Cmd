%{?scl:%scl_package perl-IPC-Cmd}

Name:           %{?scl_prefix}perl-IPC-Cmd
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.94
Release:        5%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Cmd/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
# Replace ExtUtils::MakeMaker dependency with ExtUtils::MM::Utils.
# This allows not to require perl-devel. Bug #1129443
Patch0:         IPC-Cmd-0.94-Replace-EU-MM-dependnecy-with-EU-MM-Utils.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
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
BuildRequires:  %{?scl_prefix}perl(IPC::Run) >= 0.55
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::Load::Conditional)
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
Requires:       %{?scl_prefix}perl(Params::Check) >= 0.20
Requires:       %{?scl_prefix}perl(POSIX)
Requires:       %{?scl_prefix}perl(Socket)
Requires:       %{?scl_prefix}perl(Time::HiRes)

# Filter under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Params::Check)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Params::Check\\)$
%endif

%description
IPC::Cmd allows you to run commands platform independently, interactively
if desired, but have them still work.

%prep
%setup -q -n IPC-Cmd-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Cmd.3*

%changelog
* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 1:0.94-5
- SCL

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
