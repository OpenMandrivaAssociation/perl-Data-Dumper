%define upstream_name    Data-Dumper
%define upstream_version 2.131

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    Convert data structure into perl code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.

The return value can be 'eval'ed to get back an identical copy of the
original reference structure.

Any references that are the same as one of those passed in will be named
'$VAR'_n_ (where _n_ is a numeric suffix), and other duplicate references
to substructures within '$VAR'_n_ will be appropriately labeled using arrow
notation. You can specify names for individual values to be dumped if you
use the 'Dump()' method, or you can change the default '$VAR' prefix to
something else. See '$Data::Dumper::Varname' and '$Data::Dumper::Terse'
below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.131.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.131.0-1
+ Revision: 682115
- update to new version 2.131

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.128.0-2
+ Revision: 681372
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.128.0-1mdv2011.0
+ Revision: 595095
- update to new version 2.128

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.126.0-3mdv2011.0
+ Revision: 562420
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.126.0-2mdv2011.0
+ Revision: 555743
- rebuild for perl 5.12

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 2.126.0-1mdv2010.1
+ Revision: 536126
- update to 2.126

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.125.0-1mdv2010.1
+ Revision: 474079
- import perl-Data-Dumper


* Sun Dec 06 2009 cpan2dist 2.125-1mdv
- initial mdv release, generated with cpan2dist
