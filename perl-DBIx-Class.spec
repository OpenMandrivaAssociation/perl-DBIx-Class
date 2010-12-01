%define upstream_name	 DBIx-Class
%define upstream_version 0.08124

%define _requires_exceptions %perl(DBD::Oracle\\|DBIx::Class::Admin::\\(Types\\|Descriptive\\|Usage\\))

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4
Epoch:      1

Summary:	Extensible and flexible object <-> relational mapper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Class::C3) >= 0.11
BuildRequires:	perl(Class::C3::Componentised)
BuildRequires:	perl(Class::Data::Accessor) >= 0.01
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Config::Any)
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
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(Class::C3::Componentised)
Requires:	perl(DBD::SQLite)

## scottk: The following provides are missed as they appear
##      on different lines from their "package" declarations
Provides:   perl(DBIC::SQL::Abstract)
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
Provides:	perl(DBIx::Class::SQLAHacks)
Provides:	perl(DBIx::Class::SQLMaker::Oracle)
Provides:	perl(DBIx::Class::SQLMaker::OracleJoins)
Provides:	perl(DBIx::Class::Storage)
Provides:	perl(DBIx::Class::Storage::DBIHacks)
Provides:   perl(DBIx::Class::Storage::DBI::Replicated::Types)
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
%{__perl} Makefile.PL installdirs=vendor --skipdeps
%make

%check
##export DBICTEST_PG_DSN="dbi:Pg:dbname=test;host=localhost"
##export DBICTEST_PG_USER=pgtest
##export DBICTEST_PG_PASS='pgtest'
##export DBICTEST_MYSQL_DSN="dbi:mysql:database=test;host=localhost"
##export DBICTEST_MYSQL_USER=mysqltest
##export DBICTEST_MYSQL_PASS='mysqltest'
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/dbicadmin
%{perl_vendorlib}/DBIx
%{perl_vendorlib}/SQL
%{_mandir}/man*/*
