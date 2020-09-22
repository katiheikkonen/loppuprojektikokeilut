#  Luodaan State Machine ja sen vaiheet
#  Toistaiseksi toteutus vielä malliesimerkki, mutta definition voi liittää lopullisen muodon.
#  Tällä hetkellä tehdyt kokeilut oikeasta toteutuksesta löytyy eu-central-1 Kati-Test-Machine

resource "aws_sfn_state_machine" "sentimental_analysis_state_machine" {
  name = "sentimental-analysis-state-machine"
  role_arn = aws_iam_role.role_for_state_machine_sentimental_analysis.arn
  definition = <<EOF
  {
    "Comment": "Doing sentimental analysis on the customer review with Amazon Comprehend.
    if extremely negative send to SNS topic, if fails send to SQS failure queue for further processing",
    "States": {
      "HelloWorld": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:eu-central-1:821383200340:function:analyze_with_comprehend",
        "End": true
      }
    }
  }
  EOF
  }
