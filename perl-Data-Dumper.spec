%define upstream_name    Data-Dumper
%define upstream_version 2.154

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Convert data structure into perl code

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel

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
%makeinstall_std

%clean

%files
%doc Changes
%{perl_vendorlib}/*




