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


# VPC para o GKE
resource "google_compute_network" "vpc_network" {
  name                    = "gke-vpc"
  auto_create_subnetworks = false
}

# Subrede para o Cluster
resource "google_compute_subnetwork" "subnet_gke" {
  name          = "gke-subnet"
  ip_cidr_range = "10.0.0.0/16"
  region        = var.region
  network       = google_compute_network.vpc_network.id
}

# Regra de Firewall para permitir acesso ao GKE
resource "google_compute_firewall" "allow_gke" {
  name    = "allow-gke"
  network = google_compute_network.vpc_network.id

  allow {
    protocol = "tcp"
    ports    = ["443", "10250"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["gke-node"]
}

# Cluster GKE
resource "google_container_cluster" "gke_cluster" {
  name     = "gke-cluster"
  location = var.zone
  deletion_protection = false
  network    = google_compute_network.vpc_network.id
  subnetwork = google_compute_subnetwork.subnet_gke.id

  remove_default_node_pool = true
  initial_node_count       = 1
 

  node_config {
    machine_type = "e2-micro"
    disk_size_gb = 30    # Alterado de 150 GB para 100 GB
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    tags = ["gke-node"]
    
  }
}

# Node Pool do Cluster GKE
resource "google_container_node_pool" "primary_nodes" {
  name       = "primary-node-pool"
  cluster    = google_container_cluster.gke_cluster.name
  location   = var.zone
  node_count = 2

  node_config {
    preemptible  = true
    machine_type = "e2-micro"
    disk_size_gb = 30    # Alterado de 150 GB para 100 GB
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    tags = ["gke-node"]
  }
}