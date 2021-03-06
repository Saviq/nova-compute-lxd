# Copyright 2011 Justin Santa Barbara
# Copyright 2015 Canonical Ltd
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from oslo_config import cfg

CONF = cfg.CONF

class LXDContainerDirectories(object):

    def __init__(self):
        self.base_dir = os.path.join(CONF.instances_path,
                                     CONF.image_cache_subdirectory_name)

    def get_base_dir(self):
        return self.base_dir

    def get_instance_dir(self, instance):
        return os.path.join(CONF.instances_path,
                            instance)

    def get_container_image(self, image_meta):
        return os.path.join(self.base_dir,
                            '%s.tar.gz' % image_meta.get('id'))

    def get_container_metadata(self, image_meta):
        return os.path.join(self.base_dir,
                            '%s-lxd.tar.xz' % image_meta.get('id'))

    def get_container_rootfsImg(self, image_meta):
        return os.path.join(self.base_dir,
                            '%s-root.tar.xz' % image_meta.get('id'))

    def get_container_configdrive(self, instance):
        return os.path.join(CONF.instances_path,
                            instance,
                            'config-drive')

    def get_console_path(self, instance):
        return os.path.join(CONF.lxd.root_dir,
                            'containers',
                            instance,
                            'console.log')

    def get_container_dir(self, instance):
        return os.path.join(CONF.lxd.root_dir,
                            'containers',
                            instance)

    def get_container_rootfs(self, instance):
        return os.path.join(CONF.lxd.root_dir,
                            'containers',
                            instance,
                            'rootfs')
