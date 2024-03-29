#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-kosmosfs
Version  : 0.3
Release  : 3
URL      : https://github.com/rapoth/kosmosfs/archive/release-0.3.tar.gz
Source0  : https://github.com/rapoth/kosmosfs/archive/release-0.3.tar.gz
Source1  : https://repo1.maven.org/maven2/net/sf/kosmosfs/kfs/0.3/kfs-0.3.jar
Source2  : https://repo1.maven.org/maven2/net/sf/kosmosfs/kfs/0.3/kfs-0.3.pom
Summary  : KFS Binary Package
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-kosmosfs-data = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn

%description
This package contains C++ binary distribution of KFS

%package data
Summary: data components for the mvn-kosmosfs package.
Group: Data

%description data
data components for the mvn-kosmosfs package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3/kfs-0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3/kfs-0.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3/kfs-0.3.jar
/usr/share/java/.m2/repository/net/sf/kosmosfs/kfs/0.3/kfs-0.3.pom
