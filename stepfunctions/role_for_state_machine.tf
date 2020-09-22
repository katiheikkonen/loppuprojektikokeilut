#  Yhdistetään policyt tarvittavaan rooliin ja annetaan rooli State Machinelle

resource "aws_iam_role" "role_for_state_machine_sentimental_analysis" {
  name = "role_for_state_machine_sentimental_analysis"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.eu-central-1.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": "1"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_analyze_with_comprehend_attachment" {
  role       = aws_iam_role.role_for_state_machine_sentimental_analysis.name
  policy_arn = aws_iam_policy.state_machine_iam_policy.arn
}