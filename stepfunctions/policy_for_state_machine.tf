#  Luodaan State Machinelle policy ja policy document, jotka oikeuttavat tarvittavien Lambdojen ajamiseen

resource "aws_iam_policy" "state_machine_iam_policy" {
  name        = "state_machine_iam_policy"
  description = "IAM policy with State machine access to the required Lambda Functions"
  path   = "/"
  policy = data.aws_iam_policy_document.state_machine_policy_document.json
}

data "aws_iam_policy_document" "state_machine_policy_document" {
  statement {
    sid = "statemachinepolicy"
    effect = "Allow"
    actions = [
      "lambda:InvokeFunction"
    ]
    resources = [
      "arn:aws:lambda:eu-central-1:821383200340:function:analyze_with_comprehend"
      # tähän lisätään vielä kaikki muut tarvittavat Lambdat, joita State Machine käyttää (viittaus eikä kovakoodattuna)
    ]
  }
}