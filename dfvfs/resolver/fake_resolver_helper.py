# -*- coding: utf-8 -*-
"""The fake path specification resolver helper implementation."""

# This is necessary to prevent a circular import.
import dfvfs.file_io.fake_file_io
import dfvfs.vfs.fake_file_system

from dfvfs.lib import definitions
from dfvfs.lib import errors
from dfvfs.resolver import resolver
from dfvfs.resolver import resolver_helper


class FakeResolverHelper(resolver_helper.ResolverHelper):
  """Class that implements the fake resolver helper."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_FAKE

  def OpenFileObject(self, path_spec, resolver_context):
    """Opens a file-like object defined by path specification.

    Args:
      path_spec: the VFS path specification (instance of path.PathSpec).
      resolver_context: the resolver context (instance of resolver.Context).

    Returns:
      The file-like object (instance of file_io.FileIO) or None if the path
      specification could not be resolved.
    """
    file_object = dfvfs.file_io.fake_file_io.FakeFile(resolver_context)
    file_object.open(path_spec=path_spec)
    return file_object

  def OpenFileSystem(self, path_spec, resolver_context):
    """Opens a file system object defined by path specification.

    Args:
      path_spec: the VFS path specification (instance of path.PathSpec).
      resolver_context: the resolver context (instance of resolver.Context).

    Returns:
      The file system object (instance of vfs.FakeFileSystem) or None if
      the path specification could not be resolved.
    """
    if path_spec.HasParent():
      raise errors.PathSpecError(
          u'Unsupported path specification with parent.')

    return dfvfs.vfs.fake_file_system.FakeFileSystem(resolver_context)


# Register the resolver helpers with the resolver.
resolver.Resolver.RegisterHelper(FakeResolverHelper())
