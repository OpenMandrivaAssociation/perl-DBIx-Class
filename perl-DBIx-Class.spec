%define upstream_name	 DBIx-Class
%define upstream_version 0.08270

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBD::Oracle(.*)\\)|perl\\(DBIx::Class::Admin::(.*)\\)'
%else
%define _requires_exceptions %perl(DBD::Oracle\\|DBIx::Class::Admin::\\(Types\\|Descriptive\\|Usage\\))
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Extensible and flexible object <-> relational mapper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/DBIx-Class-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Class::C3) >= 0.11
BuildRequires:	perl(Class::C3::Componentised)
BuildRequires:	perl(Class::Data::Accessor) >= 0.01
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Config::Any) >= 0.200
BuildRequires:	perl(Context::Preserve)
BuildRequires:	perl(Cwd) >= 3.19
BuildRequires:	perl(Data::Dumper::Concise)
BuildRequires:	perl(Data::Page) >= 2.00
BuildRequires:  perl(DBD::SQLite) >= 1.11
BuildRequires:  perl(DBI) >= 1.40
BuildRequires:  perl(Hash::Merge)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::Any)
BuildRequires:  perl(Math::Base36)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Path::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(SQL::Abstract) >= 1.20
BuildRequires:	perl(SQL::Abstract::Limit) >= 0.101
BuildRequires:	perl(Storable)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Builder) >= 0.33
BuildRequires:	perl(Test::Exception) >= 0.310
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Tie::StdHash)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(Variable::Magic) >= 0.440
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch

Requires:	perl(Class::C3::Componentised)
Requires:	perl(DBD::SQLite)
Requires:	perl(SQL::Abstract)

## scottk: The following provides are missed as they appear
##      on different lines from their "package" declarations
Provides:	perl(DBIC::SQL::Abstract)
Provides:	perl(DBIx::Class::_Util)
Provides:	perl(DBIx::Class::Carp)
Provides:	perl(DBIx::Class::CDBICompat::AccessorMapping)
Provides:	perl(DBIx::Class::CDBICompat::AttributeAPI)
Provides:	perl(DBIx::Class::CDBICompat::AutoUpdate)
Provides:	perl(DBIx::Class::CDBICompat::ColumnCase)
Provides:	perl(DBIx::Class::CDBICompat::ColumnGroups)
Provides:	perl(DBIx::Class::CDBICompat::Constraints)
Provides:	perl(DBIx::Class::CDBICompat::Constructor)
Provides:	perl(DBIx::Class::CDBICompat::DestroyWarning)
Provides:	perl(DBIx::Class::CDBICompat::GetSet)
Provides:	perl(DBIx::Class::CDBICompat::HasA)
Provides:	perl(DBIx::Class::CDBICompat::HasMany)
Provides:	perl(DBIx::Class::CDBICompat::ImaDBI)
Provides:	perl(DBIx::Class::CDBICompat::LazyLoading)
Provides:	perl(DBIx::Class::CDBICompat::LiveObjectIndex)
Provides:	perl(DBIx::Class::CDBICompat::MightHave)
Provides:	perl(DBIx::Class::CDBICompat::ObjIndexStubs)
Provides:	perl(DBIx::Class::CDBICompat::Pager)
Provides:	perl(DBIx::Class::CDBICompat::ReadOnly)
Provides:   perl(DBIx::Class::CDBICompat::Relationship)
Provides:	perl(DBIx::Class::CDBICompat::Retrieve)
Provides:	perl(DBIx::Class::CDBICompat::Stringify)
Provides:	perl(DBIx::Class::CDBICompat::TempColumns)
Provides:	perl(DBIx::Class::CDBICompat::Triggers)
Provides:	perl(DBIx::Class::ClassResolver::PassThrough)
Provides:	perl(DBIx::Class::Componentised)
Provides:	perl(DBIx::Class::Relationship::Accessor)
Provides:	perl(DBIx::Class::Relationship::BelongsTo)
Provides:	perl(DBIx::Class::Relationship::CascadeActions)
Provides:	perl(DBIx::Class::Relationship::HasMany)
Provides:	perl(DBIx::Class::Relationship::HasOne)
Provides:	perl(DBIx::Class::Relationship::Helpers)
Provides:	perl(DBIx::Class::Relationship::ManyToMany)
Provides:	perl(DBIx::Class::Relationship::ProxyMethods)
Provides:	perl(DBIx::Class::ResultSetProxy)
Provides:	perl(DBIx::Class::ResultSourceProxy)
Provides:	perl(DBIx::Class::ResultSource::RowParser)
Provides:	perl(DBIx::Class::ResultSource::RowParser::Util)
Provides:	perl(DBIx::Class::SQLAHacks)
Provides:	perl(DBIx::Class::SQLMaker::MSSQL)
Provides:	perl(DBIx::Class::SQLMaker::MySQL)
Provides:	perl(DBIx::Class::SQLMaker::Oracle)
Provides:	perl(DBIx::Class::SQLMaker::OracleJoins)
Provides:	perl(DBIx::Class::SQLMaker::SQLite)
Provides:	perl(DBIx::Class::Storage)
Provides:	perl(DBIx::Class::Storage::BlockRunner)
Provides:	perl(DBIx::Class::Storage::DBIHacks)
Provides:	perl(DBIx::Class::Storage::DBI::ADO::CursorUtils)
Provides:       perl(DBIx::Class::Storage::DBI::Replicated::Types)
Provides:	perl(DBIx::Class::Storage::TxnScopeGuard)
Provides:	perl(SQL::Translator::Parser::DBIx::Class)

%description
This is an SQL to OO mapper with an object API inspired by Class::DBI
(and a compatibility layer as a springboard for porting) and a
resultset API that allows abstract encapsulation of database
operations. It aims to make representing queries in your code as
perl-ish as possible while still providing access to as many of the
capabilities of the database as possible, including retrieving related
records from multiple tables in a single query, JOIN, LEFT JOIN,
COUNT, DISTINCT, GROUP BY and HAVING support.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/73oracle.t

%build
perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
##export DBICTEST_PG_DSN="dbi:Pg:dbname=test;host=localhost"
##export DBICTEST_PG_USER=pgtest
##export DBICTEST_PG_PASS='pgtest'
##export DBICTEST_MYSQL_DSN="dbi:mysql:database=test;host=localhost"
##export DBICTEST_MYSQL_USER=mysqltest
##export DBICTEST_MYSQL_PASS='mysqltest'
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/dbicadmin
%{perl_vendorlib}/DBIx
%{perl_vendorlib}/SQL
%{_mandir}/man*/*


%changelog
* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.920-1mdv2011.0
+ Revision: 673795
- update to new version 0.08192

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.910-1
+ Revision: 672612
- update to new version 0.08191

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.270-1
+ Revision: 634265
- update to new version 0.08127

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.260-1mdv2011.0
+ Revision: 628764
- new version

* Sun Dec 26 2010 Shlomi Fish <shlomif@mandriva.org> 1:0.81.240-6mdv2011.0
+ Revision: 625157
- Add a requires on SQL::Abstract which is missing and breaking many tests
- Add missing versions for BuildRequires, based on the Makefile.PL

* Wed Dec 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.240-5mdv2011.0
+ Revision: 604380
- adding all missing provides:

* Wed Dec 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.240-4mdv2011.0
+ Revision: 604305
- in fact we needed both provides

* Wed Dec 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.240-3mdv2011.0
+ Revision: 604272
- wriong provides

* Tue Nov 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.240-2mdv2011.0
+ Revision: 603778
- adding missing provides

* Fri Nov 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.240-1mdv2011.0
+ Revision: 599023
- new version

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.230-1mdv2011.0
+ Revision: 554345
- adding missing buildrequires:
- update to 0.08123

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.210-1mdv2010.1
+ Revision: 536137
- update to 0.08121

* Fri Feb 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.200-3mdv2010.1
+ Revision: 511650
- yet another requires filtering

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.200-2mdv2010.1
+ Revision: 511257
- removing extraneous requires:

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.200-1mdv2010.1
+ Revision: 510976
- update to 0.08120

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.190-2mdv2010.1
+ Revision: 506653
- removing extra requires:

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.190-1mdv2010.1
+ Revision: 506240
- update to 0.08119

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.180-1mdv2010.1
+ Revision: 502332
- update to 0.08118

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.170-1mdv2010.1
+ Revision: 502100
- update to 0.08117

* Sun Dec 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81.150-3mdv2010.1
+ Revision: 480408
- upstream patch for RT bug #52812

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.150-2mdv2010.1
+ Revision: 477725
- adding missing provides:

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.150-1mdv2010.1
+ Revision: 477624
- update to 0.08115

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.140-2mdv2010.1
+ Revision: 471641
- adding missing requires:

* Sun Nov 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.140-1mdv2010.1
+ Revision: 466151
- adding missing buildrequires:
- update to 0.08114
- using %%make macro
- update to 0.08113

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.120-1mdv2010.0
+ Revision: 447136
- update to 0.08112
- update to 0.08111

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.110-1mdv2010.0
+ Revision: 432409
- update to 0.08111

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.81.90-1mdv2010.0
+ Revision: 421136
- bumping epoch
- update to 0.08109
- update to 0.08109
- update to 0.08109
- update to 0.08109

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08108-1mdv2010.0
+ Revision: 394083
- update to new version 0.08108

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.08107-2mdv2010.0
+ Revision: 389156
- forgot to update mkrel
- fixing bug #51859

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08107-1mdv2010.0
+ Revision: 387897
- new version

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.08102-2mdv2010.0
+ Revision: 372649
- bumping mkrel
- adding missing provides

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.08102-1mdv2010.0
+ Revision: 372531
- yet another missing prereq
- adding missing prereq
- adding missing prereq
- update to 0.08012

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.08012

* Wed Sep 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08010-3mdv2009.0
+ Revision: 279935
- fix dependencies

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08010-2mdv2009.0
+ Revision: 279099
- fix dependencies

* Sun Aug 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08010-1mdv2009.0
+ Revision: 273095
- update to new version 0.08010
- new version
- new version 0.08007
- update to new version 0.08003
- revert wrong previous commit
- update to new version 0.08003
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Buchan Milne <bgmilne@mandriva.org>
    - New version 0.08006

  + Funda Wang <fwang@mandriva.org>
    - New version 0.08005

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08002-1mdv2008.0
+ Revision: 48906
- new version\nfix build


* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 22:13:46 (53645)
- Added explicit Provides: for modules hidden from PAUSE

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 16:08:38 (53466)
- import perl-DBIx-Class-0.07000-1mdv2007.0

* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 0.07000-1mdv2007.0
- Version 0.07000

* Fri Jul 14 2006 Scott Karns <scottk@mandriva.org> 0.06.999.07-1mdv2007.0
- Version 0.06999_07 (CPAN developer release)

* Tue Jul 04 2006 Scott Karns <scottk@mandriva.org> 0.06.999.05-1mdv2007.0
- Version 0.06999_05

* Tue May 23 2006 Scott Karns <scottk@mandriva.org> 0.06.003-1mdk
- First mandriva package


