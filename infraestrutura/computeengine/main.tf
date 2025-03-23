terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.15.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  zone        = var.zone
  credentials = file(var.credentials)
}

variable "project" {}
variable "region" {}
variable "zone" {}
variable "credentials" {}

resource "google_compute_network" "vpc_network" {
  name                    = "my-custom-mode-network"
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "default" {
  name          = "my-custom-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = var.region
  network       = google_compute_network.vpc_network.id
}

resource "google_compute_firewall" "ssh_rule" {
  name    = "allow-ssh"
  network = google_compute_network.vpc_network.id

  allow {
    protocol = "tcp"
    ports    = ["22", "3000", "8080"]
  }

  source_ranges = ["0.0.0.0/0"] # Permite acesso de qualquer IP
  target_tags   = ["ssh"]       # Aplica a regra apenas às VMs com essa tag
}


resource "google_compute_instance" "default" {
  name         = "flask-vm"
  machine_type = "e2-micro"
  zone         = var.zone
  tags         = ["ssh"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }


  # Install Flask
  metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential  npm openjdk-11-jdk maven python3 python3-pip rsync;pip install --upgrade flask"

  network_interface {
    subnetwork = google_compute_subnetwork.default.id

    access_config {
      # Include this section to give the VM an external IP address
    }
  }

  

}