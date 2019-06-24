#!/bin/bash

date=$(date +'%Y-%m-%d')
date_version=$(date +'%Y.%m.%d')

tool_name='cli-text-tool'
version="0.1"
starter='cli-text-tool.py'

tmp_dir=/tmp/$tool_name\__$date
deb_name=$tool_name\_$date_version
deb_dir=$tmp_dir/$deb_name

rm -R $tmp_dir

mkdir -p $deb_dir/DEBIAN

create_control() {
  echo $1 >> $deb_dir/DEBIAN/control
}

mkdir -p $deb_dir

create_control "Package: $tool_name"
create_control "Version: $version"
create_control "Security: base"
create_control "Priority: optional"
create_control "Architecture: all"
create_control "Depends: python3"
create_control "Description: Is for modifying strings in bash-scripts"

mkdir -p $deb_dir/usr/lib
cp -R -v src $deb_dir/usr/lib/$tool_name
mkdir -p $deb_dir/usr/bin
ln -s /usr/lib/$tool_name/$starter $deb_dir/usr/bin/$tool_name

dpkg-deb --build $deb_dir
cp "$deb_dir.deb" "$deb_name.deb"
rm -R $tmp_dir

