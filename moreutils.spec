%global debug_package %{nil}

Name:		moreutils
Version:	0.70
Release:	1
Source0:    https://git.joeyh.name/index.cgi/moreutils.git/snapshot/%{name}-%{version}.tar.gz
Summary:	A collection of the unix tools that nobody thought to write
URL:		https://joeyh.name/code/moreutils/
License:	GPL-2.0
Group:		System/Utils
BuildRequires:	make
BuildRequires:  docbook2x

%description
moreutils is a collection of the unix tools that nobody thought to write long
ago when unix was young.

%prep
%autosetup -p1

%build
%make_build \
    DEST=%{buildroot} \
    DOCBOOKXSL=/usr/share/sgml/docbook/xsl-stylesheets-1.79.2

%install
%make_install \
    DEST=%{buildroot} \
    DOCBOOKXSL=/usr/share/sgml/docbook/xsl-stylesheets-1.79.2

%files
%doc        README
%license    COPYING
%{_bindir}/*
%{_mandir}/man1/*.zst

