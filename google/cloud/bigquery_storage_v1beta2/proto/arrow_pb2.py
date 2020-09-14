# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery_storage_v1beta2/proto/arrow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery_storage_v1beta2/proto/arrow.proto",
    package="google.cloud.bigquery.storage.v1beta2",
    syntax="proto3",
    serialized_options=b"\n)com.google.cloud.bigquery.storage.v1beta2B\nArrowProtoP\001ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storage",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n7google/cloud/bigquery_storage_v1beta2/proto/arrow.proto\x12%google.cloud.bigquery.storage.v1beta2"(\n\x0b\x41rrowSchema\x12\x19\n\x11serialized_schema\x18\x01 \x01(\x0c"3\n\x10\x41rrowRecordBatch\x12\x1f\n\x17serialized_record_batch\x18\x01 \x01(\x0c"\xb6\x01\n\x19\x41rrowSerializationOptions\x12W\n\x06\x66ormat\x18\x01 \x01(\x0e\x32G.google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions.Format"@\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nARROW_0_14\x10\x01\x12\x0e\n\nARROW_0_15\x10\x02\x42\x87\x01\n)com.google.cloud.bigquery.storage.v1beta2B\nArrowProtoP\x01ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storageb\x06proto3',
)


_ARROWSERIALIZATIONOPTIONS_FORMAT = _descriptor.EnumDescriptor(
    name="Format",
    full_name="google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions.Format",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="FORMAT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ARROW_0_14",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ARROW_0_15",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=312,
    serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_ARROWSERIALIZATIONOPTIONS_FORMAT)


_ARROWSCHEMA = _descriptor.Descriptor(
    name="ArrowSchema",
    full_name="google.cloud.bigquery.storage.v1beta2.ArrowSchema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="serialized_schema",
            full_name="google.cloud.bigquery.storage.v1beta2.ArrowSchema.serialized_schema",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=138,
)


_ARROWRECORDBATCH = _descriptor.Descriptor(
    name="ArrowRecordBatch",
    full_name="google.cloud.bigquery.storage.v1beta2.ArrowRecordBatch",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="serialized_record_batch",
            full_name="google.cloud.bigquery.storage.v1beta2.ArrowRecordBatch.serialized_record_batch",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=140,
    serialized_end=191,
)


_ARROWSERIALIZATIONOPTIONS = _descriptor.Descriptor(
    name="ArrowSerializationOptions",
    full_name="google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="format",
            full_name="google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions.format",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_ARROWSERIALIZATIONOPTIONS_FORMAT,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=194,
    serialized_end=376,
)

_ARROWSERIALIZATIONOPTIONS.fields_by_name[
    "format"
].enum_type = _ARROWSERIALIZATIONOPTIONS_FORMAT
_ARROWSERIALIZATIONOPTIONS_FORMAT.containing_type = _ARROWSERIALIZATIONOPTIONS
DESCRIPTOR.message_types_by_name["ArrowSchema"] = _ARROWSCHEMA
DESCRIPTOR.message_types_by_name["ArrowRecordBatch"] = _ARROWRECORDBATCH
DESCRIPTOR.message_types_by_name[
    "ArrowSerializationOptions"
] = _ARROWSERIALIZATIONOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrowSchema = _reflection.GeneratedProtocolMessageType(
    "ArrowSchema",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARROWSCHEMA,
        "__module__": "google.cloud.bigquery_storage_v1beta2.proto.arrow_pb2",
        "__doc__": """Arrow schema as specified in
  https://arrow.apache.org/docs/python/api/datatypes.html and serialized
  to bytes using IPC:
  https://arrow.apache.org/docs/format/Columnar.html#serialization-and-
  interprocess-communication-ipc  See code samples on how this message
  can be deserialized.
  
  Attributes:
      serialized_schema:
          IPC serialized Arrow schema.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.ArrowSchema)
    },
)
_sym_db.RegisterMessage(ArrowSchema)

ArrowRecordBatch = _reflection.GeneratedProtocolMessageType(
    "ArrowRecordBatch",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARROWRECORDBATCH,
        "__module__": "google.cloud.bigquery_storage_v1beta2.proto.arrow_pb2",
        "__doc__": """Arrow RecordBatch.
  
  Attributes:
      serialized_record_batch:
          IPC-serialized Arrow RecordBatch.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.ArrowRecordBatch)
    },
)
_sym_db.RegisterMessage(ArrowRecordBatch)

ArrowSerializationOptions = _reflection.GeneratedProtocolMessageType(
    "ArrowSerializationOptions",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARROWSERIALIZATIONOPTIONS,
        "__module__": "google.cloud.bigquery_storage_v1beta2.proto.arrow_pb2",
        "__doc__": """Contains options specific to Arrow Serialization.
  
  Attributes:
      format:
          The Arrow IPC format to use.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions)
    },
)
_sym_db.RegisterMessage(ArrowSerializationOptions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
