# TODO
# - gkrellm2 plugin subpackage or something
Summary:	Intelligent Battery Monitor
Name:		ibam
Version:	0.5.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/ibam/%{name}-%{version}.tar.gz
# Source0-md5:	2d5222ff504dd19e7c1ea8acc2f13cf5
URL:		http://sourceforge.net/projects/ibam/
BuildRequires:	gkrellm-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBAM is an advanced battery monitor for laptops, which uses
statistical and adaptive linear methods to provide accurate
estimations of minutes of battery left or of the time needed until
full recharge.

%prep
%setup -q

%build
%{__make} ibam krell \
	CC="%{__cxx}" \
	CFLAGS='-DIBAM_VERSION=\"$(IBAM_VERSION)\" -Wall %{rpmcxxflags}'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/gkrellm2/plugins}
install -p ibam $RPM_BUILD_ROOT%{_bindir}
install -p ibam-krell.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README REPORT 
%attr(755,root,root) %{_bindir}/ibam
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/ibam-krell.so
