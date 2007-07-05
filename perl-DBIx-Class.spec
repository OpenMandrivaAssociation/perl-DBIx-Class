%define module	DBIx-Class
%define name	perl-%{module}
%define	modprefix DBIx
%define version 0.08002
%define release %mkrel 1


Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Extensible and flexible object <-> relational mapper
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/DBIx/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::C3) >= 0.11
BuildRequires:	perl(Class::Data::Accessor) >= 0.01
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Data::Page) >= 2.00
BuildRequires:  perl(DBD::SQLite) >= 1.11
BuildRequires:  perl(DBI) >= 1.40
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Find)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(SQL::Abstract) >= 1.20
BuildRequires:	perl(SQL::Abstract::Limit) >= 0.101
BuildRequires:	perl(Storable)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(JSON)
## scottk: The following provides are missed as they appear
##      on different lines from their "package" declarations
Provides:	perl(DBIx::Class::CDBICompat::ImaDBI)
Provides:	perl(DBIx::Class::CDBICompat::Constructor)
Provides:	perl(DBIx::Class::CDBICompat::Triggers)
Provides:	perl(DBIx::Class::CDBICompat::Stringify)
Provides:	perl(DBIx::Class::CDBICompat::ColumnCase)
Provides:	perl(DBIx::Class::CDBICompat::GetSet)
Provides:	perl(DBIx::Class::CDBICompat::AutoUpdate)
Provides:	perl(DBIx::Class::CDBICompat::LiveObjectIndex)
Provides:	perl(DBIx::Class::CDBICompat::ColumnGroups)
Provides:	perl(DBIx::Class::CDBICompat::AccessorMapping)
Provides:	perl(DBIx::Class::CDBICompat::HasMany)
Provides:	perl(DBIx::Class::CDBICompat::TempColumns)
Provides:	perl(DBIx::Class::CDBICompat::ObjIndexStubs)
Provides:	perl(DBIx::Class::CDBICompat::DestroyWarning)
Provides:	perl(DBIx::Class::CDBICompat::MightHave)
Provides:	perl(DBIx::Class::CDBICompat::AttributeAPI)
Provides:	perl(DBIx::Class::CDBICompat::HasA)
Provides:	perl(DBIx::Class::CDBICompat::Pager)
Provides:	perl(DBIx::Class::CDBICompat::Retrieve)
Provides:	perl(DBIx::Class::CDBICompat::Constraints)
Provides:	perl(DBIx::Class::CDBICompat::ReadOnly)
Provides:	perl(DBIx::Class::CDBICompat::LazyLoading)
Provides:	perl(DBIx::Class::Relationship::CascadeActions)
Provides:	perl(DBIx::Class::Relationship::ManyToMany)
Provides:	perl(DBIx::Class::Relationship::HasOne)
Provides:	perl(DBIx::Class::Relationship::Helpers)
Provides:	perl(DBIx::Class::Relationship::BelongsTo)
Provides:	perl(DBIx::Class::Relationship::Accessor)
Provides:	perl(DBIx::Class::Relationship::HasMany)
Provides:	perl(DBIx::Class::Relationship::ProxyMethods)
Provides:	perl(DBIx::Class::Storage)
Provides:	perl(DBIx::Class::ResultSetProxy)
Provides:	perl(DBIx::Class::ClassResolver::PassThrough)
Provides:	perl(DBIx::Class::Componentised)
Provides:	perl(DBIx::Class::ResultSourceProxy)
Provides:	perl(SQL::Translator::Parser::DBIx::Class)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor
%make

%check
##export DBICTEST_PG_DSN="dbi:Pg:dbname=test;host=localhost"
##export DBICTEST_PG_USER=pgtest
##export DBICTEST_PG_PASS='pgtest'
##export DBICTEST_MYSQL_DSN="dbi:mysql:database=test;host=localhost"
##export DBICTEST_MYSQL_USER=mysqltest
##export DBICTEST_MYSQL_PASS='mysqltest'
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/dbicadmin
%{perl_vendorlib}/%{modprefix}
%{perl_vendorlib}/SQL
%{_mandir}/man*/*





