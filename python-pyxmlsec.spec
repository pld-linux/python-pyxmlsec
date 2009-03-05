Summary:	Python bindings for XML Security Library
Name:		python-pyxmlsec
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://labs.libre-entreprise.org/download.php/430/pyxmlsec-%{version}.tar.gz
# Source0-md5:	150631f634654804076f73a0859fea1a
URL:		http://pypyxmlsec.sourceforge.net/
BuildRequires:	nss-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	xmlsec1-devel
BuildRequires:	xmlsec1-openssl-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXMLSec is a set of Python bindings for XML Security Library
(XMLSec).

%prep
%setup -q -n pyxmlsec-%{version}

%build
echo "1" | env CFLAGS="%{rpmcflags} -I/usr/include/xmlsec1" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%py_postclean

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README docs/html
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/*.egg-info
%{_examplesdir}/%{name}-%{version}
