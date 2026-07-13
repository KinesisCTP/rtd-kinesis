.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 92416cbe-d475-4bc4-be54-8830c8d22f63

===================================
AI Workstation - DGX Spark - NVIDIA
===================================

.. container:: equipment-kicker

   NVIDIA · DGX Spark


.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - NVIDIA
   * - **Model**
     - DGX Spark
   * - **Equipment class**
     - AI Workstation
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active
   * - **Training**
     - Required
   * - **Risk assessment**
     - Not currently listed as required
   * - **Primary contact**
     - Samuel A. Prieto (sxp8070)


Overview
--------

The NVIDIA DGX Spark is a purpose-built AI workstation powered by NVIDIA Grace Blackwell technology, designed for advanced AI development, model training, and inference workloads with exceptional performance and energy efficiency.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Operating system**
     - Ubuntu 22.04 LTS
   * - **Processor**
     - NVIDIA Grace CPU: 72 Arm Neoverse V2 cores
   * - **Graphics / accelerator**
     - NVIDIA Blackwell GPU: 192GB HBM3e memory, NVLink connectivity
   * - **System memory**
     - 480 GB
   * - **Storage**
     - 4TB NVMe SSD
   * - **Networking**
     - Dual 100GbE networking
   * - **Additional specifications**
     - Grace Blackwell Superchip architecture, AI performance up to 2.5 petaFLOPS, 1.4kW max power consumption

Typical workflows
-----------------

1. Train and fine-tune large language models and multimodal AI models
2. Run inference workloads for production AI applications
3. Develop and test AI agents and autonomous systems
4. Process large-scale datasets for computer vision and NLP
5. Prototype and benchmark AI algorithms before deploying to larger clusters

Software & dependencies
-----------------------

- NVIDIA AI Enterprise software suite
- CUDA Toolkit
- cuDNN
- TensorRT
- PyTorch
- TensorFlow
- JAX
- NVIDIA NeMo Framework

Access, training & booking
--------------------------

Access restricted to authorized personnel. Schedule intensive workloads to minimize conflicts with other users.

- **Training:** Hands-on training is required before operation.

Safety & operating limits
-------------------------

.. warning::

   Schedule compute-intensive jobs during off-peak hours when possible. Monitor GPU memory usage and close completed jobs promptly. Maintain proper ventilation around the system. Do not interrupt running training jobs without coordination with other users. Follow lab data management policies for storing models and datasets.

**Operational controls**

- Training required

- **Software licence:** Required.



Keywords
--------

``AI`` · ``workstation`` · ``GPU`` · ``DGX`` · ``NVIDIA`` · ``Grace Blackwell`` · ``deep learning`` · ``machine learning`` · ``inference`` · ``training`` · ``compute``


.. note::

   For current availability or details not recorded here, contact
   Samuel A. Prieto (sxp8070).
