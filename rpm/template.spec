Name:           ros-indigo-message-generation
Version:        0.2.10
Release:        0%{?dist}
Summary:        ROS message_generation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/message_generation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gencpp
Requires:       ros-indigo-genlisp
Requires:       ros-indigo-genmsg
Requires:       ros-indigo-genpy
BuildRequires:  ros-indigo-catkin

%description
Package modeling the build-time dependencies for generating language bindings of
messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.10-0
- Autogenerated by Bloom

