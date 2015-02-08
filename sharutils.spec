Summary:	GNU shar utils
Name:		sharutils
Version:	4.15
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	http://ftp.gnu.org/gnu/sharutils/%{name}-%{version}.tar.xz
# Source0-md5:	4b94e8016adf1a544c90e96132e36c8d
URL:		http://www.gnu.org/software/sharutils/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.14
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sharutils package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar). This
format can be sent through email (which can be problematic for regular
binary files). The shar utility supports a wide range of capabilities
(compressing, uuencoding, splitting long files for multi-part
mailings, providing checksums), which make it very flexible at
creating shar files. After the files have been sent, the unshar tool
scans mail messages looking for shar files. Unshar automatically
strips off mail headers and introductory text and then unpacks the
shar files.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/shar
%attr(755,root,root) %{_bindir}/unshar
%attr(755,root,root) %{_bindir}/uudecode
%attr(755,root,root) %{_bindir}/uuencode
%{_infodir}/sharutils.info*
%{_mandir}/man[15]/*.[15]*

