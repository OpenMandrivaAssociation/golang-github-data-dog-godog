# Run tests in check section
%bcond_without check

%global goipath         github.com/DATA-DOG/godog
Version:                0.7.8

%global common_description %{expand:
The official Cucumber BDD framework for Golang.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Official Cucumber BDD framework for Golang
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  golang(github.com/DATA-DOG/go-txdb)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build  
%gobuildroot
%gobuild -o _bin/godog %{goipath}/cmd/godog


%install
%goinstall
install -Dpm 0755 _bin/godog %{buildroot}%{_bindir}/godog


%if %{with check}
%check
%gochecks examples
%endif


%files
%license LICENSE
%{_bindir}/godog


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md examples


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.8-1
- Release 0.7.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.6-1
- First package for Fedora

