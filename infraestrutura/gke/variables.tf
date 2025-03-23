variable "project" {
  description = "ID do Projeto GCP"
  type        = string
}

variable "region" {
  description = "Região para o GKE"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "Zona para o GKE"
  type        = string
  default     = "us-central1-c"
}

variable "credentials" {
  description = "Caminho para o arquivo JSON da Service Account"
  type        = string
}