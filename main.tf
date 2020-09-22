#Nimetään provider
provider "aws" {
  region = "eu-west-2" #kova koodattuna, mutta myöhemmin mapattuna
  #access_key = ""
  #secret_key = ""
}
module "sns" {
  source = "./sns"
}
